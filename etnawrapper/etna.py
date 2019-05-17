#!/usr/bin/env python3
"""Client for ETNA's APIs"""
# TODO: Implement a Session upon instantiation?
# TODO: Cli ? :o
# TODO: CLI.
from typing import Union
from io import BytesIO

import requests

from .constants import (
    AUTH_URL,
    IDENTITY_URL,
    USER_INFO_URL,
    PROMOTION_URL,
    USER_PROMO_URL,
    ACTIVITY_URL,
    NOTIF_URL,
    GRADES_URL,
    PICTURE_URL,
    SEARCH_URL,
    ACTIVITIES_URL,
)


__author__ = 'Theo Massard <massar_t@etna-alternance.net>'


class EtnaWrapper:
    """"""
    def __init__(self, login: str, password: str = None, cookies: dict = None, use_session: bool = False):
        self.login = login
        self._cookies = cookies
        if cookies is None:
            self._cookies = self.get_cookies(login, password)
        # XXX: be careful about this one
        if use_session:
            self._req = requests.Session()
        else:
            self._req = requests

    def _query(self, url: str, method='GET', raw: bool = False, data=None) -> Union[dict, requests.Response]:
        """Perform a request using the `self._req` HTTP client.

        Upon requesting a non-standard URL (not returning JSON),
        the `raw` flag allow to return a `requests.Response` object
        instead of a dictionnary.
        """
        response = self._req.request(
            method,
            url,
            cookies=self._cookies,
            json=data,
            headers=self.headers,
            timeout=50
        )
        if raw:
            return response
        return response.json()

    @staticmethod
    def get_cookies(login: str = None, password: str = None) -> str:
        """Fetch a Cookie."""
        if login is None:
            raise ValueError("missing login, can not authenticate")
        if password is None:
            raise ValueError("missing password, can not authenticate")
        data = {
            'login': login,
            'password': password
        }
        resp = requests.post(AUTH_URL, data=data)
        return resp.cookies.get_dict()

    def get_user_info(self, user_id: int = None) -> dict:
        """Return a user's informations. Defaults to self.login."""
        # TODO: Docstring -> show example
        url = IDENTITY_URL
        if user_id is not None:
            url = USER_INFO_URL.format(user_id=user_id)
        result = self._query(url)
        return result

    def get_promotion(self, promotion_id: int = None) -> dict:
        """Return a user's informations. Defaults to self.login."""
        # TODO: Docstring -> show example
        # NOTE: Is it actually the same output?
        url = USER_PROMO_URL
        if promotion_id is not None:
            url = PROMOTION_URL.format(promo_id=promotion_id)
        result = self._query(url)
        return result

    def get_current_activities(self, login: str = None) -> dict:
        """Return a user's current activities.

        Defaults to self.login.

        """
        url = ACTIVITY_URL.format(login or self.login)
        result = self._query(url)
        return result

    def get_notifications(self, login: str = None) -> dict:
        """Return `login`'s notifications.

        If login is not set, defaults to self.login.
        """
        url = NOTIF_URL.format(login or self.login)
        result = self._query(url)
        return result

    def get_grades(self, promotion_id: int, login: str = None) -> dict:
        """Fetch a student's grades, based on the promotion."""
        url = GRADES_URL.format(login=login or self.login, promo_id=promotion_id)
        result = self._query(url)
        return result

    def get_picture(self, login: str = None) -> BytesIO:
        url = PICTURE_URL.format(login=login or self.login)
        result = self._query(url, raw=True)
        return result.content

    def get_projects(self, login: str = None) -> dict:
        """Fetch a student's projects base on the login."""
        url = SEARCH_URL.format(login=login or self.login)
        result = self._query(url)
        return result

    def get_project_activites(self, module: str) -> dict:
        """Fetch activities related to `module`."""
        url = ACTIVITIES_URL.format(module_id=module)
        result = self._query(url)
        return result


class OldWrapper:
    """Simple HTTP client."""

    def get_group_for_activity(self, module=None, project=None, **kwargs):
        """Get groups for activity.

        :param str module: Base module
        :param str module: Project which contains the group requested
        :return: JSON
        """

        _module_id = kwargs.get('module', module)
        _project_id = kwargs.get('project', project)
        _url = GROUPS_URL.format(module_id=_module_id, project_id=_project_id)
        return self._request_api(url=_url).json()

    def get_students(self, **kwargs):
        """Get users by promotion id.

        :param int promotion: Promotion ID
        :return: JSON
        """

        _promotion_id = kwargs.get('promotion')
        _url = PROMOTION_URL.format(promo_id=_promotion_id)
        return self._request_api(url=_url).json()

    def get_log_events(self, login=None, **kwargs):
        """Get a user's log events.

        :param str login: User's login (Default: self.login)
        :return: JSON
        """

        _login = kwargs.get(
            'login',
            login
        )
        log_events_url = GSA_EVENTS_URL.format(login=_login)
        return self._request_api(url=log_events_url).json()

    def get_events(self, login=None, start_date=None, end_date=None, **kwargs):
        """Get a user's events.

        :param str login: User's login (Default: self.login)
        :param str start_date: Start date
        :param str end_date: To date
        :return: JSON
        """

        _login = kwargs.get(
            'login',
            login
        )
        log_events_url = EVENTS_URL.format(
            login=_login,
            start_date=start_date,
            end_date=end_date,
        )
        return self._request_api(url=log_events_url).json()

    def get_logs(self, login=None, **kwargs):
        """Get a user's logs.

        :param str login: User's login (Default: self.login)
        :return: JSON
        """

        _login = kwargs.get(
            'login',
            login
        )
        log_events_url = GSA_LOGS_URL.format(login=_login)
        return self._request_api(url=log_events_url).json()


__all__ = (
    'EtnaWrapper',
)
