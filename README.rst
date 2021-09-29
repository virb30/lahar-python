Lahar Python: Python wrapper for LAHAR API
=================

*Lahar Python* helps you to integrate your python based systems
with the mailmarketing software provided by LAHAR.

Inspired by the official `lahar-ruby <https://github.com/LAHAR-APP/lahar-ruby>` package.

Usage
======

Install:

.. code-block:: console
    pip install lahar-python

Then use it on wherever you need.

#. Import the ``Client`` object:

    .. code-block:: python
        from lahar import Client

#. Create a ``client`` object passing the API token as parameter.
    optionally you can change the ``event`` (defaults to ``integration``)

    .. code-block:: python
        client = Client('api-token', event='integration')

#. Call the method to send data to the API:

    .. code-block:: python
        # import the LeadStage Enum
        from lahar import LeadStage

        # create a dict with the data (check the LAHAR api docs for the available keys)
        data = dict(email_contato='valid@email.com')
        # create a new lead (sends the data to /conversions endpoint
        client.create_lead(data)

        # update a leadstage
        new_stage = LeadStage.CLIENT
        client.change_lead_status(data, new_stage)


Contribute
=======

Your contribution is welcome.

Setup your development enviroment:

    .. code-block:: console
        git clone git@github.com:virb30/lahar-python.git
        cd lahar-python
        python -m venv .venv
        source .venv/bin/activate
        # or .venv\Scripts\activate on windows
        pip install -r requirements.txt
        python -m unittest


License
========
The MIT License (MIT)

Copyright (c) 2021 Vinicius Boscoa

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.