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
peers="bb87f624ab412739e54cdffadc3fc97831e1d42f@85.174.199.64:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,64fc57fb297ef839da5212b391cf27b32fe7ab8a@109.123.243.55:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,907c1095ae2abea4e5a6ba568f1fc6aa719a0d47@38.242.146.53:39656,39ce82b6613c327f2bbc4cedc3a25dbf0bf8094e@38.242.252.137:26656,5b1771d56334354c3415d27f521dd9922fa149e4@185.218.126.186:26656,a5455fdd70a915023bb4902143704430793c3e68@162.55.163.78:26656,ca91b6230e92ee6f5b9c5b1fe80fa07a1b72225a@185.211.6.205:26656,6903fcc270cb5189033124fece49ce4bb4745ba0@38.242.245.13:26656,0e90ac8e15b040c2a158b68f25299fc32a9d5940@89.117.57.25:26656,3e7ff1b1fa8626812b1ab8acf84a8b60518a8c10@65.109.88.254:34656,2fe037c0e7a8f3da20ef50f20712b55fd52a9b8b@144.91.110.211:29656,9bf81d292a0cb72a1920b50d63dd1dc881ed0a2f@5.199.138.18:39656,cb825bccee49827c07dce19878c8790c67222a54@91.107.132.237:26656,74f4a995c2a878a06bcbf69d5377adb6cbe0a91d@89.117.63.122:26656,cf13f41c223c6e47e581f6ae8ec7c554218de8fc@207.244.251.201:26656,f4a8fb180fbbb4c44e7721368cbc6ce3f9fc47e1@5.189.140.55:26656,385e57b19ab9d142b27bd0b4db3d8d84c83947e6@77.120.115.135:39656,5e04ee4edf672b798326f00a5f1520a952a1952e@94.103.89.5:26656,3af13cf1fdd2483ecb19ee9f77918455498bb53d@154.26.158.49:26656,5950cd437c087192fbc71c25b5070d12a6066f23@46.151.27.109:26656,e4f4184e37647a28418368bf5f299d696c1d3d3b@184.174.35.12:26656,2ce838eea29c3f6ca650081dd0fa99186304b151@37.99.82.28:26656,668f3f60a0ff3f9fcbaf8551782f71de1cc767a9@89.116.24.215:26656,785ffb99f8724319d44254cbb47b3428aaaa25a5@38.242.236.134:26656,19d3a6f510b01e17a972211850d386bf3f0c395d@77.232.43.16:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
