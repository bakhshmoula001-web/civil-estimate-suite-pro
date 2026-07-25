
class IssueReceiptRegister:
    def __init__(self, ledger):
        self.ledger=ledger

    def receipt(self, material, qty, ref=""):
        self.ledger.add_transaction(material,"RECEIPT",qty,ref)

    def issue(self, material, qty, ref=""):
        self.ledger.add_transaction(material,"ISSUE",qty,ref)
