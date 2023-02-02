# DEPRECATED #

DummyAuthenticator is now a [part of JupyterHub core](https://github.com/jupyterhub/jupyterhub/blob/4e7936056744cdad31d608388a349207196efa56/jupyterhub/auth.py#L1122). 
You can migrate to it by setting:

```python
c.JupyterHub.authenticator_class = "dummy"
```

The JupyterHub documentation has more information on [how to setup a development environment](https://jupyterhub.readthedocs.io/en/stable/contributing/setup.html)

# Dummy JupyterHub Authenticator #

Simple authenticator for [JupyterHub](http://github.com/jupyter/jupyterhub/)
that allows all user logins regardless of password. Useful only for testing,
do not use for anything actually serious!

## Installation ##

```
cd /opt/tljh/hub/lib/python3.6/site-packages
git clone https://github.coma/revotechuet/tljhi2gauthenticator
```

Should install it. It has no additional dependencies beyond JupyterHub.

You can then use this as your authenticator by adding the following line to
your `jupyterhub_config.py`:

```
vim /opt/tljh/hub/lib/python3.6/site-packages/tljh/jupyterhub_config.py
c.JupyterHub.authenticator_class = 'tljhi2gauthenticator.I2GAuthenticator'
```

