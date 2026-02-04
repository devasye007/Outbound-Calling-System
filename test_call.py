import asyncio
from livekit import api
from livekit.protocol.sip import CreateSIPParticipantRequest

TRUNK_ID = "ST_3oo8qHoqrQ52"      # your LiveKit outbound trunk ID
TO_NUMBER = "+97142798200"      # number you want to call

async def make_call():
    lk = api.LiveKitAPI()

    req = CreateSIPParticipantRequest(
        sip_trunk_id=TRUNK_ID,
        sip_call_to=TO_NUMBER,
        room_name="first-test-call",
        participant_identity="outbound-test",
        participant_name="Nurse Recruitment",
        wait_until_answered=True
    )

    print("Placing call...")
    await lk.sip.create_sip_participant(req)
    print("Call request sent.")

asyncio.run(make_call())
  
