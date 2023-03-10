# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)




## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: [https://nibiru-testnet.grpc.kjnodes.com](https://nibiru-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (43)
```bash
peers="e7f86d445265b364e7da43e1b0ab77063b255f0a@45.140.185.171:26656,9799db8d7117b0eff6ef5a179e8b09be7b25cbdb@157.245.64.100:26656,7a108d369433a8ce88db2f844a896fc5bffbd764@212.23.222.89:35656,591b00c0bfdda9f94e40128869041d1da9ee1639@149.102.152.77:26656,4d343a3fcafa9ff022869003a40a0e308b4bc29c@193.46.243.122:26656,aedf05252d5fac762d5732ab1bc8728a3337b81d@185.197.195.13:26656,51265dc8904e791fb6b02703efafe6b1ef593f82@89.248.192.120:26656,4e12fec38b3fb61ad2502a007351dcf65020fd7b@185.208.206.224:26656,25d7a6c32516f18e3f45b0379460d8ed4e396b43@164.92.84.68:26656,b402b5605e266dc7844fd20223082d798fee5dec@34.172.227.227:26656,cdc4fa8458e3225cc61b45ae6708cc5ccc0f2d18@38.242.153.228:26656,bf10da2792c9439edbfccce2cf0852e692039112@185.215.180.237:26656,00321c2d0049ddfcfe51bdec8fc8b264c5d1a36d@185.197.251.186:26656,05beef8bd94ad31ce038f13d67db3a3c36539ac5@62.141.44.89:39656,e432e664883c6eaea8d2b62fdb16a20ea81997d3@167.71.213.250:26656,4eb0cc5fa9727b3c1803536e9fe48b045cb9923e@194.60.201.124:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,f55ce3e7e95379654cc43f7d840d88f41eaaccec@118.69.175.70:26656,9f7c112d00333e12d11ebebb2a90c3a9a18be028@80.82.215.250:39656,b300cdfbbd9af83bab94fcfc493d43a88ab01acc@80.82.215.214:39656,b6db16ab4d2dfd61d0be94df4738ce5f1913de11@212.41.9.98:26656,55dfbbffebc40b147b2b765fc65a65711dafcbcd@31.220.78.145:39656,5490ce086f118de22b6225d050578e91f45bf8eb@194.163.176.132:26656,377b116d7bb48b5dc3b9fe33b4c2464faf15d818@89.117.55.215:26656,5b4b12ded2c0db5f29345580b507156ca5399053@31.220.84.69:26656,d3ddfe8ad75847df085262b9cdbc49b29ce30ba6@35.229.110.80:26656,dc82088dce51fdba9585c29ea87a72ed1c0723fa@79.137.248.192:26656,99673ce0ffb7df09b9464ea16bc5678a49e0e424@13.251.1.89:10656,91d0512ebcedb3f4ab9f26ae13b67166ce7a7003@46.180.223.102:26656,abf4334bf998a54bffb99335bd07fcf3b4bea130@185.249.225.73:38656,82d8f0d473863b8f104623539b0c4b65a997318a@146.190.226.211:26656,20791e6708172528675c75346e3354b7d2222007@38.242.211.6:26656,55ebd6fc24f8dbbd9057b80653e5cef7e25d574f@149.102.152.75:26656,35eaab9bffc5af4d91da1ffc920833ccd4a150a6@89.116.28.96:26656,0d321d5390f5c58dcc0b9680a48c11d2e1ce7dad@65.109.162.26:36656,f9889b46126c058840df70cd280b8dac580f39d6@38.242.135.215:26656,df6c645c8acc777fe7d31ee1348c1e8d54f3cd33@65.108.1.16:26656,c73f013c571cbc5e21b1f97d942ce9742008203c@142.132.132.200:21656,ee821bf9562168acd1276b206bffd40ff5817f7f@89.117.58.196:26656,92060aa4b4f9103aaf78010f0d987015564bc211@154.26.158.200:26656,2393cd0e22a8c70f34526fcddc99e08478c3cb7a@89.117.53.2:26656,bb85d394004d779a500dbb2943df163a5f278bcb@46.101.185.15:38656,4003c942d2fd79c1ef289673a01561681a49ec03@194.163.153.41:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
