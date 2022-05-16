# TEMPLATE used for automatic script submission of multiple datasets

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'SUS-RunIISummer20UL18MiniAOD-stau250_lsp1_ctau1000mm_v4'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../../python/SUS-RunIISummer20UL18MiniAODv2_cfg.py'

config.JobType.maxJobRuntimeMin = 5*60
config.JobType.maxMemoryMB = 2500

config.section_("Data")

config.Data.inputDataset = '/SUS-RunIISummer20UL18GEN-stau250_lsp1_ctau1000mm_v4/myshched-RECO-b48a278ad9b80207fe073529bf32d66e/USER'
config.Data.inputDBS = 'phys03'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1

config.Data.outLFNDirBase = '/store/user/myshched/mc/UL2018-pythia-v4'
config.Data.publication = True
config.Data.outputDatasetTag = 'MiniAOD'

config.section_("Site")
config.Site.whitelist = ['T2_DE_DESY']
config.Site.storageSite = 'T2_DE_DESY'