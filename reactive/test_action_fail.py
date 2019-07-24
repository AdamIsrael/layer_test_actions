"""Test action-fail messaging.

Testing how action-fail messages are returned.
"""
from charms.reactive import when, when_not, set_flag, clear_flag
from charmhelpers.core.hookenv import (
    action_fail,
    action_set,
)

@when_not('test-action-fail.installed')
def install_test_action_fail():
    set_flag('test-action-fail.installed')


@when('actions.test-success')
def action_test_success():
    action_set({
        'success': True,
    })
    clear_flag('actions.test-success')


@when('actions.test-failure')
def action_test_failure():
    action_set({
        'success': False,
    })
    action_fail('This action has failed.')
    clear_flag('actions.test-failure')
