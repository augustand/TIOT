__author__ = 'bergus'


@app.route("/")
def hello():
    print '\n\n\n\n\n\n'
    print onlineClient.getClients()
    print '\n\n\n\n\n\n'
    return render_template('/client.html')
