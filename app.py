from flask import Flask, render_template, request, flash
from forms import CurrencyConverterForm
from converter import convert_currency, is_valid_currency_code

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CurrencyConverterForm()

    if request.method == 'POST' and form.validate_on_submit():
        from_currency = form.from_currency.data
        to_currency = form.to_currency.data
        amount = form.amount.data

        if not is_valid_currency_code(from_currency) or not is_valid_currency_code(to_currency):
            flash('Invalid currency code. Please enter a valid code.', 'error')
        elif not amount.isdigit():
            flash('Invalid amount. Please enter a valid number.', 'error')
        else:
            converted_amount = convert_currency(from_currency, to_currency, float(amount))
            flash(f'The converted amount is {converted_amount}', 'success')

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
