import collections


def meeting_planner(slotsA, slotsB, dur):
    # return first time slot that works for both user of
    # time duration dur
    # time slots are disjointed
    event = collections.namedtuple('event', ('s', 'e'))

    def to_event(slot):
        # well formed input assumes start and end for each nested element
        start, end = slot[0], slot[1]
        return event(start, end)
    print(event)
    eventsA = collections.deque([to_event(sub_list_a) for sub_list_a in slotsA])
    print(eventsA[0])


slotsA = [[60, 61], [60, 120], [140, 210]]
slotsB = [[0, 68], [101, 102]]
dur = 8
meeting_planner(slotsA,slotsB,8)
'''
    eventsA = collections.deque([to_event(sub_list_a) for sub_list_a in slotsA])
    eventsB = collections.deque([to_event(sub_list_b) for sub_list_b in slotsB])

    # now that we have are list of events objects - iterate through both
    # attempting to find an intersection
    # Bs__As____Be___Ae , As__Bs____Ae__Be , disjoint: As__Ae Bs__Be

    # bs_____As_____Ae___Be and As___Bs___Be___Ae
    curr_time = None
    while eventsA and eventsB:
        curr_a, curr_b = eventsA[0], eventsB[0]

        curr_dur = None
        max_s, min_e = max(curr_a.s, curr_b.s), min(curr_a.e, curr_b.e)
        potential_dur = min_e - max_s
        if potential_dur >= dur: return [max_s, max_s + dur]

        # determine who we are going to pop
        curr_time = min(curr_b.e, curr_a.e)
        if curr_time == curr_b.e:
            eventsB.popleft()
        else:
            eventsA.popleft() 
'''