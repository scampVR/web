import json

POH_CONTRACT_ADDRESS = '0xC5E9dDebb09Cd64DfaCab4011A0D5cEDaf7c9BDb'

_poh_contract = None

EIP_1271_ABI = '[{"constant":true,"inputs":[{"name":"_messageHash","type":"bytes32"},{"name":"_signature","type":"bytes"}],"name":"isValidSignature","outputs":[{"name":"magicValue","type":"bytes4"}],"payable":false,"stateMutability":"view","type":"function"}]'

def is_valid_eip_1271_signature(web3, address, hash, signature) -> bool:
    try:
        eip_1271_contract = web3.eth.contract(address=address, abi=json.loads(EIP_1271_ABI))
        retval = eip_1271_contract.functions.isValidSignature(hash, signature).call()
        return web3.toInt(retval) == 0x1626ba7e
    except Exception as e:
        return False

def get_poh_contract(web3):
    global _poh_contract
    if _poh_contract is None:
        _poh_contract = web3.eth.contract(address=POH_CONTRACT_ADDRESS, abi=POH_ABI)

    return _poh_contract


def is_registered_on_poh(web3, address: str) -> bool:
    return get_poh_contract(web3).functions.isRegistered(address).call()


POH_ABI = [{"inputs":[{"internalType":"contract IArbitrator","name":"_arbitrator","type":"address"},{"internalType":"bytes","name":"_arbitratorExtraData","type":"bytes"},{"internalType":"string","name":"_registrationMetaEvidence","type":"string"},{"internalType":"string","name":"_clearingMetaEvidence","type":"string"},{"internalType":"uint256","name":"_submissionBaseDeposit","type":"uint256"},{"internalType":"uint64","name":"_submissionDuration","type":"uint64"},{"internalType":"uint64","name":"_renewalPeriodDuration","type":"uint64"},{"internalType":"uint64","name":"_challengePeriodDuration","type":"uint64"},{"internalType":"uint256[3]","name":"_multipliers","type":"uint256[3]"},{"internalType":"uint64","name":"_requiredNumberOfVouches","type":"uint64"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_submissionID","type":"address"},{"indexed":False,"internalType":"uint256","name":"_requestID","type":"uint256"}],"name":"AddSubmission","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_submissionID","type":"address"},{"indexed":True,"internalType":"uint256","name":"_challengeID","type":"uint256"},{"indexed":False,"internalType":"enum ProofOfHumanity.Party","name":"_party","type":"uint8"},{"indexed":True,"internalType":"address","name":"_contributor","type":"address"},{"indexed":False,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"AppealContribution","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"contract IArbitrator","name":"_arbitrator","type":"address"},{"indexed":True,"internalType":"address","name":"_governor","type":"address"},{"indexed":False,"internalType":"uint256","name":"_submissionBaseDeposit","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_submissionDuration","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_challengePeriodDuration","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_requiredNumberOfVouches","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_sharedStakeMultiplier","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_winnerStakeMultiplier","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_loserStakeMultiplier","type":"uint256"}],"name":"ArbitratorComplete","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_submissionID","type":"address"},{"indexed":True,"internalType":"uint256","name":"_requestID","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_challengeID","type":"uint256"}],"name":"ChallengeResolved","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"contract IArbitrator","name":"_arbitrator","type":"address"},{"indexed":True,"internalType":"uint256","name":"_disputeID","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_metaEvidenceID","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_evidenceGroupID","type":"uint256"}],"name":"Dispute","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"contract IArbitrator","name":"_arbitrator","type":"address"},{"indexed":True,"internalType":"uint256","name":"_evidenceGroupID","type":"uint256"},{"indexed":True,"internalType":"address","name":"_party","type":"address"},{"indexed":False,"internalType":"string","name":"_evidence","type":"string"}],"name":"Evidence","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_submissionID","type":"address"},{"indexed":True,"internalType":"uint256","name":"_challengeID","type":"uint256"},{"indexed":False,"internalType":"enum ProofOfHumanity.Party","name":"_side","type":"uint8"}],"name":"HasPaidAppealFee","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint256","name":"_metaEvidenceID","type":"uint256"},{"indexed":False,"internalType":"string","name":"_evidence","type":"string"}],"name":"MetaEvidence","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_submissionID","type":"address"},{"indexed":False,"internalType":"uint256","name":"_requestID","type":"uint256"}],"name":"ReapplySubmission","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_requester","type":"address"},{"indexed":True,"internalType":"address","name":"_submissionID","type":"address"},{"indexed":False,"internalType":"uint256","name":"_requestID","type":"uint256"}],"name":"RemoveSubmission","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"contract IArbitrator","name":"_arbitrator","type":"address"},{"indexed":True,"internalType":"uint256","name":"_disputeID","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_ruling","type":"uint256"}],"name":"Ruling","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_submissionID","type":"address"},{"indexed":True,"internalType":"uint256","name":"_requestID","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_challengeID","type":"uint256"}],"name":"SubmissionChallenged","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_submissionID","type":"address"},{"indexed":True,"internalType":"address","name":"_voucher","type":"address"}],"name":"VouchAdded","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_submissionID","type":"address"},{"indexed":True,"internalType":"address","name":"_voucher","type":"address"}],"name":"VouchRemoved","type":"event"},{"constant":False,"inputs":[{"internalType":"string","name":"_evidence","type":"string"},{"internalType":"string","name":"_name","type":"string"}],"name":"addSubmission","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[{"internalType":"address[]","name":"_submissionIDs","type":"address[]"},{"internalType":"string[]","name":"_evidence","type":"string[]"},{"internalType":"string[]","name":"_names","type":"string[]"}],"name":"addSubmissionManually","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_submissionID","type":"address"}],"name":"addVouch","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"arbitratorDataList","outputs":[{"internalType":"contract IArbitrator","name":"arbitrator","type":"address"},{"internalType":"uint96","name":"metaEvidenceUpdates","type":"uint96"},{"internalType":"bytes","name":"arbitratorExtraData","type":"bytes"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"arbitratorDisputeIDToDisputeData","outputs":[{"internalType":"uint96","name":"challengeID","type":"uint96"},{"internalType":"address","name":"submissionID","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"challengePeriodDuration","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_submissionID","type":"address"},{"internalType":"enum ProofOfHumanity.Reason","name":"_reason","type":"uint8"},{"internalType":"address","name":"_duplicateID","type":"address"},{"internalType":"string","name":"_evidence","type":"string"}],"name":"challengeRequest","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[{"internalType":"contract IArbitrator","name":"_arbitrator","type":"address"},{"internalType":"bytes","name":"_arbitratorExtraData","type":"bytes"}],"name":"changeArbitrator","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"uint64","name":"_submissionDuration","type":"uint64"},{"internalType":"uint64","name":"_renewalPeriodDuration","type":"uint64"},{"internalType":"uint64","name":"_challengePeriodDuration","type":"uint64"}],"name":"changeDurations","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_governor","type":"address"}],"name":"changeGovernor","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"uint256","name":"_loserStakeMultiplier","type":"uint256"}],"name":"changeLoserStakeMultiplier","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"string","name":"_registrationMetaEvidence","type":"string"},{"internalType":"string","name":"_clearingMetaEvidence","type":"string"}],"name":"changeMetaEvidence","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"uint64","name":"_requiredNumberOfVouches","type":"uint64"}],"name":"changeRequiredNumberOfVouches","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"uint256","name":"_sharedStakeMultiplier","type":"uint256"}],"name":"changeSharedStakeMultiplier","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_submissionID","type":"address"},{"internalType":"address[]","name":"_vouches","type":"address[]"},{"internalType":"bytes[]","name":"_signatures","type":"bytes[]"},{"internalType":"uint256[]","name":"_expirationTimestamps","type":"uint256[]"}],"name":"changeStateToPending","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"uint256","name":"_submissionBaseDeposit","type":"uint256"}],"name":"changeSubmissionBaseDeposit","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"uint256","name":"_winnerStakeMultiplier","type":"uint256"}],"name":"changeWinnerStakeMultiplier","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"_submissionID","type":"address"},{"internalType":"uint256","name":"_requestID","type":"uint256"},{"internalType":"address","name":"_duplicateID","type":"address"}],"name":"checkRequestDuplicates","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_submissionID","type":"address"}],"name":"executeRequest","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_submissionID","type":"address"},{"internalType":"uint256","name":"_challengeID","type":"uint256"},{"internalType":"enum ProofOfHumanity.Party","name":"_side","type":"uint8"}],"name":"fundAppeal","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_submissionID","type":"address"}],"name":"fundSubmission","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":True,"inputs":[],"name":"getArbitratorDataListCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"_submissionID","type":"address"},{"internalType":"uint256","name":"_requestID","type":"uint256"},{"internalType":"uint256","name":"_challengeID","type":"uint256"}],"name":"getChallengeInfo","outputs":[{"internalType":"uint16","name":"lastRoundID","type":"uint16"},{"internalType":"address","name":"challenger","type":"address"},{"internalType":"uint256","name":"disputeID","type":"uint256"},{"internalType":"enum ProofOfHumanity.Party","name":"ruling","type":"uint8"},{"internalType":"uint64","name":"duplicateSubmissionIndex","type":"uint64"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"_submissionID","type":"address"},{"internalType":"uint256","name":"_requestID","type":"uint256"},{"internalType":"uint256","name":"_challengeID","type":"uint256"},{"internalType":"uint256","name":"_round","type":"uint256"},{"internalType":"address","name":"_contributor","type":"address"}],"name":"getContributions","outputs":[{"internalType":"uint256[3]","name":"contributions","type":"uint256[3]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"_submissionID","type":"address"},{"internalType":"uint256","name":"_requestID","type":"uint256"}],"name":"getNumberOfVouches","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"_submissionID","type":"address"},{"internalType":"uint256","name":"_requestID","type":"uint256"}],"name":"getRequestInfo","outputs":[{"internalType":"bool","name":"disputed","type":"bool"},{"internalType":"bool","name":"resolved","type":"bool"},{"internalType":"bool","name":"requesterLost","type":"bool"},{"internalType":"enum ProofOfHumanity.Reason","name":"currentReason","type":"uint8"},{"internalType":"uint16","name":"nbParallelDisputes","type":"uint16"},{"internalType":"uint16","name":"lastChallengeID","type":"uint16"},{"internalType":"uint16","name":"arbitratorDataID","type":"uint16"},{"internalType":"address payable","name":"requester","type":"address"},{"internalType":"address payable","name":"ultimateChallenger","type":"address"},{"internalType":"uint8","name":"usedReasons","type":"uint8"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"_submissionID","type":"address"},{"internalType":"uint256","name":"_requestID","type":"uint256"},{"internalType":"uint256","name":"_challengeID","type":"uint256"},{"internalType":"uint256","name":"_round","type":"uint256"}],"name":"getRoundInfo","outputs":[{"internalType":"bool","name":"appealed","type":"bool"},{"internalType":"uint256[3]","name":"paidFees","type":"uint256[3]"},{"internalType":"enum ProofOfHumanity.Party","name":"sideFunded","type":"uint8"},{"internalType":"uint256","name":"feeRewards","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"_submissionID","type":"address"}],"name":"getSubmissionInfo","outputs":[{"internalType":"enum ProofOfHumanity.Status","name":"status","type":"uint8"},{"internalType":"uint64","name":"submissionTime","type":"uint64"},{"internalType":"uint64","name":"index","type":"uint64"},{"internalType":"bool","name":"registered","type":"bool"},{"internalType":"bool","name":"hasVouched","type":"bool"},{"internalType":"uint256","name":"numberOfRequests","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"governor","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"_submissionID","type":"address"}],"name":"isRegistered","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"loserStakeMultiplier","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_submissionID","type":"address"},{"internalType":"uint256","name":"_requestID","type":"uint256"},{"internalType":"uint256","name":"_iterations","type":"uint256"}],"name":"processVouches","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"string","name":"_evidence","type":"string"},{"internalType":"string","name":"_name","type":"string"}],"name":"reapplySubmission","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_submissionID","type":"address"},{"internalType":"string","name":"_evidence","type":"string"}],"name":"removeSubmission","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_submissionID","type":"address"}],"name":"removeSubmissionManually","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_submissionID","type":"address"}],"name":"removeVouch","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"renewalPeriodDuration","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"requiredNumberOfVouches","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"uint256","name":"_disputeID","type":"uint256"},{"internalType":"uint256","name":"_ruling","type":"uint256"}],"name":"rule","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"sharedStakeMultiplier","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"submissionBaseDeposit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"submissionCounter","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"submissionDuration","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_submissionID","type":"address"},{"internalType":"string","name":"_evidence","type":"string"}],"name":"submitEvidence","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"vouches","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"winnerStakeMultiplier","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address payable","name":"_beneficiary","type":"address"},{"internalType":"address","name":"_submissionID","type":"address"},{"internalType":"uint256","name":"_requestID","type":"uint256"},{"internalType":"uint256","name":"_challengeID","type":"uint256"},{"internalType":"uint256","name":"_round","type":"uint256"}],"name":"withdrawFeesAndRewards","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[],"name":"withdrawSubmission","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"}]
