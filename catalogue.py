# https://opendata.cern.ch/docs/cms-simulated-dataset-names
# https://opendata.cern.ch/docs/cms-guide-for-condition-database
# ERA                       CMSSW          Docker
# 2011-2012 proton-proton ; CMSSW_5_3_32 ; cmsopendata/cmssw_5_3_32-slc6_amd64_gcc472

Run = {
    # 2011 p-p datasets
    '7TeV' : {
        # Metadata
        'MetaData' : {
            'GJSON'   : { 'Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON.txt' : 'http://opendata.web.cern.ch/record/1001' }, 
            'GT_DATA' : 'FT_53_LV5_AN1',
            'GT_MC'   : 'START53_LV6A1'
        }
        # Data
        'SingleElectron' : {
            'RunA' : 'https://opendata.cern.ch/record/31',
            'RunB' : 'https://opendata.cern.ch/record/284'
        },
        'DoubleElectron' : {
            'RunA' : 'https://opendata.cern.ch/record/16',
            'RunB' : 'https://opendata.cern.ch/record/271'
        },
        'SingleMu' : {
            'RunA' : 'https://opendata.cern.ch/record/32',
            'RunB' : 'https://opendata.cern.ch/record/285'
        },
        'DoubleMu' : {
            'RunA' : 'https://opendata.cern.ch/record/17',
            'RunB' : 'https://opendata.cern.ch/record/272'
        },
        'MuEG' : {
            'RunA' : 'https://opendata.cern.ch/record/25',
            'RunB' : 'https://opendata.cern.ch/record/278'
        },
        'MuOnia' : {
            'RunA' : 'https://opendata.cern.ch/record/27',
            'RunB' : 'https://opendata.cern.ch/record/280'
        },
        # MC
        'JPsiToMuMu_2MuPEtaFilter' : 'https://opendata.cern.ch/record/1335',
        'DYJetsToLL_M-10To50'      : 'https://opendata.cern.ch/record/1393',
        'DYJetsToLL_M-50'          : 'https://opendata.cern.ch/record/1394'
    },
    # 2012 p-p dataset
    '8TeV' : {
        # Metadata
        'MetaData' : {
            'GJSON'   : { 'Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt' : 'http://opendata.web.cern.ch/record/1002' },
            'GT_DATA' : 'FT53_V21A_AN6_FULL',
            'GT_MC'   : 'START53_V27'
        },
        # Data
        'SingleElectron' : {
            'RunB' : 'https://opendata.cern.ch/record/6020',
            'RunC' : 'https://opendata.cern.ch/record/6046'
        },
        'DoubleElectron' : {
            'RunB' : 'https://opendata.cern.ch/record/6003',
            'RunC' : 'https://opendata.cern.ch/record/6029'
        },
        'SingleMu' : {
            'RunB' : 'https://opendata.cern.ch/record/6021',
            'RunC' : 'https://opendata.cern.ch/record/6047'
        },
        'DoubleMuParked' : {
            'RunB' : 'https://opendata.cern.ch/record/6004',
            'RunC' : 'https://opendata.cern.ch/record/6030'
        },
        'MuEG' : {
            'RunB' : 'https://opendata.cern.ch/record/6014',
            'RunC' : 'https://opendata.cern.ch/record/6040'
        },
        'MuOnia' : {
            'RunB' : 'https://opendata.cern.ch/record/6016',
            'RunC' : 'https://opendata.cern.ch/record/6042'
        },
        # MC
        'DYJetsToLL_M-50'      : 'https://opendata.cern.ch/record/7730' ,
        'DY1JetsToLL_M-50_ext' : 'https://opendata.cern.ch/record/7719',
        'DY1JetsToLL_M-10To50' : 'https://opendata.cern.ch/record/7718',
        'DY3JetsToLL_M-50'     : 'https://opendata.cern.ch/record/7722',
        'DY1JetsToLL_M-10To50' : 'https://opendata.cern.ch/record/7718',
    },
    # aod 2015
    '13TeV' : {
        # Metadata
        'MetaData' : {
            'GJSON'   : '',
            'GT_DATA' : '76X_dataRun2_16Dec2015_v0',
            'GT_MC'   : '76X_mcRun2_asymptotic_RunIIFall15DR76_v1'
        },
        # Data
        'SingleElectron' : {
            'RunD' : 'http://opendata.web.cern.ch/record/24103'   
        },
        'SingleMuon' : {
            'RunD' : 'http://opendata.web.cern.ch/record/24102'
        },
        'DoubleMuon' : {
            'RunD' : 'http://opendata.web.cern.ch/record/24110'
        },
        'DoubleMuonLowMass' : {
            'RunD' : 'http://opendata.web.cern.ch/record/24109'
        },
        'MuonEG' : {
            'RunD' : 'http://opendata.web.cern.ch/record/24104'
        },
        'DoubleEG' : {
            'RunD' : 'http://opendata.web.cern.ch/record/24115'
        },
        'MuOnia' : {
            'RunD' : 'http://opendata.web.cern.ch/record/24105'
        },
        
        # MC (miniaod)
        'DYJetsToLL_M-50_LO'           : 'https://opendata.cern.ch/record/16466',
        'DYJetsToLL_M-50_LO-ext1'      : 'https://opendata.cern.ch/record/16465',
        'DYJetsToLL_M-50_NLO'          : 'https://opendata.cern.ch/record/16459',
        'DYJetsToLL_M-5to50_LO'        : 'https://opendata.cern.ch/record/16478',
        'DYJetsToLL_M-10to50_NLO'      : 'https://opendata.cern.ch/record/16428',
        'DYJetsToLL_M-10to50_NLO-ext1' : 'https://opendata.cern.ch/record/16429',
        'DYJetsToLL_M-10to50_NLO-ext3' : 'https://opendata.cern.ch/record/16430',
    }
}
