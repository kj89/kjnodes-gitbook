# Services

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
peers="b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,cf13f41c223c6e47e581f6ae8ec7c554218de8fc@207.244.251.201:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,aa999ecb4e74d0b95465638670cd6fddc9c1f544@65.109.89.37:26656,9df18d7fe13517817100466c2c7980c6125354b7@136.243.172.166:26656,b2ce119c318844778f33dc3dc544dce62572c45a@183.2.149.136:26656,a4bc4bfb7e2af517eaef8baebf5f404a0b65f59f@217.76.51.182:10656,96285853644bd5c35db33b033abfed598c9c10c0@75.119.130.70:26656,2ce838eea29c3f6ca650081dd0fa99186304b151@37.99.82.28:26656,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656,fee8c13c90bc44816ad3b6dbca1d1044008b1b87@65.21.106.157:26656,11c7655bc96c229a3d18ca3bbe7d8944ce645aab@89.117.59.191:26656,24b9df9d8b731fe559a749a76d7466c6646c2d23@65.21.200.124:26656,6601866c96263ccdffc009edbfa2150855f41ab1@38.242.226.88:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,23a7f6ab77328d3459418e71dd284ad5a832624f@109.205.181.113:26656,54306de2385188258eebdffb7cd1bd5614266245@109.205.182.51:26656,5db2f2c82ba2b9c431d069270ebc16d35985ffaa@91.230.110.96:26656,bf5be00eb2fed367f75b63b9c685ab612765e302@149.102.139.163:26656,6dac2f8baeb71ccc594f0633d957ec9c8dc66b26@82.208.23.76:26656,e8010a62d188bcc5c2c74e669e380faccbccd106@185.197.250.246:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,64cf20514a03108936e27b9382c228d42b4642e1@88.198.14.157:26656,4432207b04118601f777ac93a5c3dd441b968734@70.34.250.4:26656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656,3db2fea3bb460cf3668cbc328433e39d030f565a@109.123.243.101:26656,04c7b4c7b1ca40e04e767925c08846d2951f5425@34.23.168.27:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
