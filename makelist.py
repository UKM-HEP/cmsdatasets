import os
from catalogue import Run

cwd = os.getcwd()

docker_copy="docker run --privileged -v ${PWD}/XX_COM_XX:/code:rw -it --rm cernopendata/cernopendata-client download-files --recid XX_RECID_XX --no-expand --protocol xrootd"

# COM
for icom in Run:
    # datasets
    COM_PATH = '%s/%s' %( cwd , icom )
    if not os.path.exists( COM_PATH ) : os.system('mkdir -p %s' %COM_PATH )
    cmdcopy = docker_copy.replace( 'XX_COM_XX' , icom )
    
    for ipd, datasets in Run[icom].items():
        if ipd == 'MetaData' : continue
        isData = type(datasets) is dict
        if isData:
            # run period
            for iperiod, url in datasets.items():
                print( "Primary Datasets : %s-%s" %( ipd , iperiod ) )
                RECID_DATA = url.split('/')[-1]
                cmdcopy_exec = cmdcopy.replace( 'XX_RECID_XX' , RECID_DATA )
                os.system(cmdcopy_exec)
                os.system( 'mv %s/%s/*.txt %s/' %( COM_PATH , RECID_DATA , COM_PATH ) )
                os.system( 'rm -rf %s/%s' %( COM_PATH , RECID_DATA ) )
        else:
            print( "MonteCarlo Datasets : ", ipd )
            RECID_MC = datasets.split('/')[-1]
            cmdcopy_exec = cmdcopy.replace( 'XX_RECID_XX' , RECID_MC )
            os.system(cmdcopy_exec)
            os.system( 'mv %s/%s/*.txt %s/' %( COM_PATH , RECID_MC , COM_PATH ) )
            os.system( 'rm -rf %s/%s' %( COM_PATH , RECID_MC ) )
