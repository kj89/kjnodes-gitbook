# Services

[installation](./installation/ "mention") [upgrade](./upgrade/ "mention") [snapshot](./snapshot/ "mention") [state-sync](./state-sync/ "mention") [useful-commands](./useful-commands/ "mention")

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibirufi) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:39090

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

**live-peers** (28)
```bash
peers="c414545b963134299a3c64a7d6386c9c4f7bd417@93.183.208.88:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656,cf13f41c223c6e47e581f6ae8ec7c554218de8fc@207.244.251.201:26656,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656,668f3f60a0ff3f9fcbaf8551782f71de1cc767a9@89.116.24.215:26656,d31e21c9ddc00e2ab2bbfbafde3810e2d4370993@31.220.94.117:39656,11c7655bc96c229a3d18ca3bbe7d8944ce645aab@89.117.59.191:26656,385e57b19ab9d142b27bd0b4db3d8d84c83947e6@77.120.115.135:39656,9174c2c90723a515a6303513abf6444eb13aba8c@45.85.249.107:26656,fcdabba02ea5bc305e5b285c4f768cdad5df4380@94.131.112.29:39656,2ce838eea29c3f6ca650081dd0fa99186304b151@37.99.82.28:26656,15bb498412ae171d617fec5525c6be0536fa7352@94.158.152.162:26656,6028bf33e78679aec8db8c7bcf8024705dd74b8e@95.216.148.212:26656,4e60470d4e89d6bc76f9f48bfb4a99a0f0341a4c@176.124.221.194:26656,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,db1deb2f4d23eb91da1d10e86562d84aaa0f9a0e@5.75.239.226:26656,bb7c79e9d370dc8ff87c2810f9196aaaa8d9f8ae@65.108.68.119:26656,40b36393a266c76ef0218284d868641e69ce1b57@185.135.137.216:26656,64fc57fb297ef839da5212b391cf27b32fe7ab8a@109.123.243.55:26656,e9a824e54f1161a85a3044f48968ee28404ce5fc@183.2.149.136:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,33bae0a8e95d0adc364b5feb44a766100b927e86@91.196.164.89:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,5e8e5ca5fe3ffa7987093a91b63edc15f2e6bb4d@194.60.201.205:26656,8b46bc0515e53eae52acd8b6c89e90faaf132dc3@93.183.208.84:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
