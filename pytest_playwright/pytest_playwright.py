import pytest
from typing import Any

def pytest_addoption(parser: Any) -> None:
    group = parser.getgroup("playwright", "Playwright")
    group.addoption(
        "--browser",
        action="append",
        default=[],
        help="Browser engine which should be used",
        choices=["chromium", "firefox", "webkit"],
    )
    group.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run tests in headed mode.",
    )
    group.addoption(
        "--browser-channel",
        action="store",
        default=None,
        help="Browser channel to be used.",
    )
    group.addoption(
        "--slowmo",
        default=0,
        type=int,
        help="Run tests with slow mo",
    )
    group.addoption(
        "--device", default=None, action="store", help="Device to be emulated."
    )
    group.addoption(
        "--output",
        default="test-results",
        help="Directory for artifacts produced by tests, defaults to test-results.",
    )
    group.addoption(
        "--tracing",
        default="off",
        choices=["on", "off", "retain-on-failure"],
        help="Whether to record a trace for each test.",
    )
    group.addoption(
        "--video",
        default="off",
        choices=["on", "off", "retain-on-failure"],
        help="Whether to record video for each test.",
    )
    group.addoption(
        "--screenshot",
        default="off",
        choices=["on", "off", "only-on-failure"],
        help="Whether to automatically capture a screenshot after each test.",
    )
    group.addoption(
        "--full-page-screenshot",
        action="store_true",
        default=False,
        help="Whether to take a full page screenshot",
    )

def pytest_configure(config: pytest.Config):
    if config.pluginmanager.hasplugin("asyncio"):
        from pytest_playwright.asyncio import PytestPlaywrightAsyncio

        config.pluginmanager.register(PytestPlaywrightAsyncio())
    else:
        from pytest_playwright.sync import PytestPlaywrightSync

        config.pluginmanager.register(PytestPlaywrightSync())
