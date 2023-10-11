#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Desc   : unittest of st_plan

from examples.st_game.plan.st_plan import _should_react, _choose_retrieved, _wait_react

from examples.st_game.tests.plan.test_converse import init_two_roles


def test_should_react():
    role_ir, role_km = init_two_roles()
    roles = {
        role_ir.name: role_ir,
        role_km.name: role_km
    }

    observed = role_ir.observe()
    retrieved = role_ir.retrieve(observed)

    focused_event = _choose_retrieved(role_ir, retrieved)

    reaction_mode = _should_react(role_ir, focused_event, roles)  # chat with Isabella Rodriguez
    assert "chat with" in reaction_mode


def test_wait_react():
    role_ir, role_km = init_two_roles("July1_the_ville_isabella_maria_klaus-step-3-1")
    reaction_mode = "wait: February 13, 2023, 00:01:30"
    f_daily_schedule = role_ir.scratch.f_daily_schedule
    # [['sleeping', 360], ['waking up and completing her morning routine (getting out of bed)', 5], ['sleeping', 180]]

    _wait_react(role_ir, reaction_mode)
    new_f_daily_schedule = role_ir.scratch.f_daily_schedule
    # [['sleeping', 360], ['waking up and completing her morning routine (getting out of bed)', 5],
    # ['waking up and completing her morning routine (brushing her teeth)', 5], ['sleeping', 180]]
    assert len(f_daily_schedule) == len(new_f_daily_schedule)