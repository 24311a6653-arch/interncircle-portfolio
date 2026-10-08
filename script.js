let expenses = JSON.parse(localStorage.getItem("expenses")) || [];

function addExpense() {
    const date = document.getElementById("date").value;
    const category = document.getElementById("category").value;
    const amount = document.getElementById("amount").value;
    const description = document.getElementById("description").value;

    if (!date || !category || !amount || !description) {
        alert("Please fill all fields.");
        return;
    }

    const expense = {
        date: date,
        category: category,
        amount: Number(amount),
        description: description
    };

    expenses.push(expense);

    localStorage.setItem("expenses", JSON.stringify(expenses));

    displayExpenses();
    displaySummary();

    document.getElementById("date").value = "";
    document.getElementById("category").value = "";
    document.getElementById("amount").value = "";
    document.getElementById("description").value = "";
}

function displayExpenses() {
    const list = document.getElementById("expenseList");

    list.innerHTML = "";

    expenses.forEach(function(expense) {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${expense.date}</td>
            <td>${expense.category}</td>
            <td>₹${expense.amount}</td>
            <td>${expense.description}</td>
        `;

        list.appendChild(row);
    });
}

function displaySummary() {
    const summary = document.getElementById("summary");

    let totals = {};

    expenses.forEach(function(expense) {
        if (totals[expense.category]) {
            totals[expense.category] += expense.amount;
        } else {
            totals[expense.category] = expense.amount;
        }
    });

    summary.innerHTML = "";

    for (let category in totals) {
        const p = document.createElement("p");
        p.textContent = category + ": ₹" + totals[category];
        summary.appendChild(p);
    }
}

function downloadCSV() {
    if (expenses.length === 0) {
        alert("No expenses to download.");
        return;
    }

    let csv = "Date,Category,Amount,Description\n";

    expenses.forEach(function(expense) {
        csv += `${expense.date},${expense.category},${expense.amount},${expense.description}\n`;
    });

    const blob = new Blob([csv], { type: "text/csv" });
    const url = URL.createObjectURL(blob);

    const link = document.createElement("a");
    link.href = url;
    link.download = "expenses.csv";
    link.click();

    URL.revokeObjectURL(url);
}

displayExpenses();
displaySummary();