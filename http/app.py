"""
Simple PySide6 desktop client for the /api/patients REST service.

Requirements:
  pip install PySide6 requests

Usage:
  python app.py   # assumes API at https://disp.yxl.ch/

Change API_BASE below if necessary.
"""

from PySide6.QtCore import Qt, Slot
import sys
import requests
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox,QListWidget)


import os
os.environ['no_proxy'] = '*'

API_BASE = "https://disp.yxl.ch"
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}

def handle_response(resp):
    """Return JSON or raise for HTTP error."""
    try:
        # TODO: The API returns a JSON string, extract JSON from the response.
        data = resp.json()
        return data

    except ValueError:
        resp.raise_for_status()
        return {}
        if not resp.ok:
            raise RuntimeError(data.get("error", resp.text))
            return data


def api_get_all():
    """
    TODO: send GET to API_BASE
    Should return a list of patient dicts, e.g. [{"id":1, "name":"Alice","age":30}, …]
    """
    url = f"{API_BASE}/api/patients"
    response = requests.get(url, headers=HEADERS, verify=False,timeout=8)
    return handle_response(response)



def api_get(pid):
    """
    TODO: send GET to f"{API_BASE}/{pid}"
    Should return a single patient dict, e.g. {"id":1,"name":"Alice","age":30}
    """
    url = f"{API_BASE}/api/patients/{pid}"
    response = requests.get(url)
    return handle_response(response)



def api_create(name, age):
    """
    TODO: send POST to API_BASE with json payload {"name":name,"age":age}
    Should return the created patient dict.
    """
    url = f"{API_BASE}/api/patients"
    payload = {"name": name, "age": age}

    response = requests.post(url, json=payload, headers=HEADERS, verify=False)

    return handle_response(response)


def api_update(pid, name, age):
    """
    TODO: send PUT to f"{API_BASE}/{pid}" with json {"name":name,"age":age}
    Should return the updated patient dict.
    """
    url = f"{API_BASE}/api/patients/{pid}"
    payload = {"name": name, "age": age}

    response = requests.put(url, json=payload)

    return handle_response(response)


def api_delete(pid):
    """
    TODO: send DELETE to f"{API_BASE}/{pid}"
    Should return an empty dict or confirmation.
    """
    url = f"{API_BASE}/api/patients/{pid}"
    response = requests.delete(url)

    return handle_response(response)



class PatientClient(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Patient Manager")
        self.resize(420, 320)

        layout = QVBoxLayout(self)
        # List of patients
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)
        self.list_widget.itemSelectionChanged.connect(self.populate_fields)

        # Form row
        form = QHBoxLayout()
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Name")
        self.age_edit = QLineEdit()
        self.age_edit.setPlaceholderText("Age")
        self.age_edit.setFixedWidth(60)
        form.addWidget(QLabel("Name:"))
        form.addWidget(self.name_edit)
        form.addWidget(QLabel("Age:"))
        form.addWidget(self.age_edit)
        layout.addLayout(form)

        # Buttons
        btn_row = QHBoxLayout()
        self.add_btn = QPushButton("Add")
        self.update_btn = QPushButton("Update")
        self.delete_btn = QPushButton("Delete")
        btn_row.addWidget(self.add_btn)
        btn_row.addWidget(self.update_btn)
        btn_row.addWidget(self.delete_btn)
        layout.addLayout(btn_row)

        # Connect signals
        self.add_btn.clicked.connect(self.add_patient)
        self.update_btn.clicked.connect(self.update_patient)
        self.delete_btn.clicked.connect(self.delete_patient)

        self.refresh()

    # ----------------- API helpers -----------------
    def refresh(self):
        """Reload list from API"""
        self.list_widget.clearSelection()
        self.list_widget.clear()
        try:
            for p in api_get_all():
                self.list_widget.addItem(f"{p['id']}: {p['name']} ({p['age']})")
        except Exception as exc:
            QMessageBox.critical(self, "API Error", str(exc))

    def selected_id(self):
        item = self.list_widget.currentItem()
        return int(item.text().split(":")[0]) if item else None

    # ----------------- slots -----------------
    @Slot()
    def populate_fields(self):
        pid = self.selected_id()
        if pid is None:
            self.name_edit.clear()
            self.age_edit.clear()
            return
        try:
            patient = api_get(pid)
            self.name_edit.setText(patient.get('name', ''))
            self.age_edit.setText(str(patient.get('age', '')))
        except Exception:
            # Patient might have been deleted meanwhile -> clear fields
            self.name_edit.clear()
            self.age_edit.clear()

    @Slot()
    def add_patient(self):
        name = self.name_edit.text().strip()
        age = self.age_edit.text().strip()
        if not name or not age.isdigit():
            QMessageBox.warning(self, "Input", "Enter valid name and integer age")
            return
        try:
            api_create(name, int(age))
            self.refresh()
            self.name_edit.clear()
            self.age_edit.clear()
        except Exception as exc:
            QMessageBox.critical(self, "Error", str(exc))

    @Slot()
    def update_patient(self):
        pid = self.selected_id()
        if pid is None:
            QMessageBox.information(self, "Select", "Select a patient to update")
            return
        name = self.name_edit.text().strip()
        age = self.age_edit.text().strip()
        if not name or not age.isdigit():
            QMessageBox.warning(self, "Input", "Enter valid name and integer age")
            return
        try:
            api_update(pid, name, int(age))
            self.refresh()
        except Exception as exc:
            QMessageBox.critical(self, "Error", str(exc))

    @Slot()
    def delete_patient(self):
        pid = self.selected_id()
        if pid is None:
            QMessageBox.information(self, "Select", "Select a patient to delete")
            return
        if QMessageBox.question(self, "Confirm", "Delete selected patient?") == QMessageBox.Yes:
            try:
                api_delete(pid)
                self.refresh()
                self.name_edit.clear()
                self.age_edit.clear()
            except Exception as exc:
                QMessageBox.critical(self, "Error", str(exc))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PatientClient()
    window.show()
    sys.exit(app.exec())
