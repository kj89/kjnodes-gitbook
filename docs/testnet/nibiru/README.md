# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" alt=""><figcaption></figcaption></figure>

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

**live-peers** (27)
```bash
peers="dd80caf5a8080ef255a181e06f89d5fcf0dac15c@65.108.232.182:11656,cf13f41c223c6e47e581f6ae8ec7c554218de8fc@207.244.251.201:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,736c0d6962c283e49ac4b4c1d2df4e9335d9923c@38.242.145.186:26656,aa999ecb4e74d0b95465638670cd6fddc9c1f544@65.109.89.37:26656,4432207b04118601f777ac93a5c3dd441b968734@70.34.250.4:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,385e57b19ab9d142b27bd0b4db3d8d84c83947e6@77.120.115.135:39656,e9a824e54f1161a85a3044f48968ee28404ce5fc@183.2.149.136:26656,452a3e2dda1f044221f30a8e25e6b90eaef70ce1@154.26.157.17:26656,cf755b5d8b1c400dd003221e461d717a8535c007@83.167.103.221:26656,0e90ac8e15b040c2a158b68f25299fc32a9d5940@89.117.57.25:26656,481fcddc51ad2695ef829cd8449d64b7988895db@164.92.250.88:26656,5c052c78ab48d0b26098574ba8b04e039209769a@95.217.1.96:26656,24b9df9d8b731fe559a749a76d7466c6646c2d23@65.21.200.124:26656,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656,5f895db09fecaac3f6d1cd595ccd897c57eb6215@195.2.70.240:26656,5db2f2c82ba2b9c431d069270ebc16d35985ffaa@91.230.110.96:26656,f18044f2eba474d62f491d2df1cbf704fe671c5d@178.18.247.73:26656,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656,e4f4184e37647a28418368bf5f299d696c1d3d3b@184.174.35.12:26656,d88eb958f18940d75add40b51d2a69295ed9e378@5.75.245.162:26656,de5eef4a640ca1c05e0f4b5102ace1e531c88478@38.242.154.181:26656,151add3a88c91fdcfce837a58eee8d8d8c9bf960@31.220.84.73:26656,bc60bfcadd0f0d5ea25a9b7165303f26b67d4365@185.217.125.43:26656,6a6a3155ca2465ad6d5da0589e4143c77eeb73f4@91.242.229.71:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
