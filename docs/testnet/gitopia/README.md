# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (35)
```
peers="648416f708c52248a00c5ad3912387a353c26548@178.63.102.172:44656,4977214dacb3713797653c1bc07b5982bcc91649@142.132.253.112:51656,5c2c2b27e1824097d4f5dc7a581a8d615923e76f@185.252.235.110:41656,fd3c90536aafeb61fb735ca15fec7cb1f0747f8c@77.91.73.34:656,182a0faf787f0f62ac2af8975d951ab94573d7d2@194.195.87.52:41656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,5c74fe6868cda2003926c0a6299c9cebec5c4d1a@65.21.239.60:41656,4ec16520a171af24269ddb7aa57f555a455bc76d@95.111.247.144:26656,fb0a1c5dbc329b1b0ae3dac6776df4eb5f2072f6@79.137.248.142:26656,6fa19dbe0236fc9328513ced95d9dd6f8330dbf3@34.160.118.165:26656,0bd2f1a11791f043abba0c10c6792c9f1e29cf22@188.166.82.173:656,9684d6a5fbdac8dc075579dd719e3f78e6be97af@142.93.38.14:26656,ccf24b1e4f8566f3914c08e13d2b6154ed47ddbd@45.153.48.45:26656,3b7845f8c8361c2f2de742473cd891c6e8cdeabf@83.171.249.159:656,995177c4b8c2b498de50483a614f9e30bf02e843@65.109.130.180:26656,e511a5b55979b7d630f016e2b15b513690fd3e33@185.239.209.124:656,3e5ba61e8481c6c71d3f2cc022dd6671ed7cacf8@65.21.170.3:41656,c5fa8b2df54c71b7a6479d9ba67dcd87b7109f25@103.104.75.230:41656,e79532749fb5dd95366f4568a7b2430d0e316fb5@84.46.255.163:26656,67e839cff368a20c9b7a1390b739d3538866b0b6@65.21.134.202:26356,8884a6a17d1634de0d7c177c352d9adcc2b672b4@165.22.7.77:41656,38f4e436b28b05850fa9b67cadf0700123cec094@45.10.154.166:26656,a0004e1861bb5430c8e80a89df5528cd6f3afe44@1.15.73.234:26656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,edae8278cef6113e38af80504fb83cbf5eb0f023@165.232.129.242:26656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,74a4bbfbf4d1ca9852d10f3a97e4d012c62aec9e@146.190.102.111:41656,ad33cf22f96e43448798686ed0f7428b8fdacf5b@5.161.90.174:656,e1ab0573d55ff92fad55d2929e353904f1bbe36f@135.181.16.252:31656,df66a0896a1f6cac3ad45810346c1d096b42adc9@164.92.80.120:26656,6871aeacd353d66c38b1ebbf3b1ad244fa05e32b@167.86.84.125:26656,31099d763305ead833b84c28b142ecbfd3628a64@85.190.246.250:41656,374da78901e59810277fc35482bce6e30953f488@80.79.6.155:41656,4ceba74efb843cf10926a9ec757e4e2081d71e92@207.244.226.183:656,6ea375302fdd319ef64e013f469e286faf739da8@213.239.207.165:20086"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
