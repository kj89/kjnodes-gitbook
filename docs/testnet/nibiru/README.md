# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)



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

**live-peers** (29)
```bash
peers="b282a25e8ad8cb6a002b9f432d29d1e57a63aeea@65.109.89.23:39656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,391ce347a9f0745a1f50126fcc1f9a878bacd8fe@184.174.32.55:26656,96f253c371a7f7f854faf7ffc5e0ee9fc4f8dd7f@165.227.32.93:26656,1da145d81ca9d5d9ccd55f529435056a27fcdeef@184.174.34.227:26656,daeabf9286ea1331f07f7981c5425aeca5db1f5b@95.217.5.233:26656,f4a8fb180fbbb4c44e7721368cbc6ce3f9fc47e1@5.189.140.55:26656,42c34c76c4c1fa2f32a8c28849cba28549f71a03@109.123.243.27:26656,afe25edd4b7515d5f013112166e157e4289177bb@95.217.35.186:46656,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,0b66c11e20e2f759da3b9d96d8712b615136563e@65.108.11.50:26656,a02783c0eb8917ba8a186ea644aacb343148f825@74.234.48.72:26656,ad41ef68f4740d5be84ff54c34b0331b02ff4ae4@85.10.193.246:29656,f4fa2e13e64628d96f9158a6a2afbb19ebac574e@85.190.246.120:26656,f31536c1f70fb1a8127c1f412bbccef4d1a19e20@195.14.6.2:26656,93b0696cd10a3d683c1cf28641ff210d316954da@89.117.63.232:26656,90d2b3055fc4a27fcdb4dd472c087830ecf8e42c@84.46.248.35:26656,349a3441e26e7dc8a1d76f69d0acfc820942c837@89.163.215.4:39656,6b69faf2cd1287de0c12e04aefcde72b6578ce40@82.208.21.249:26656,6c37c542748d1d78c3c0d96eb7c5f1af5ee6a770@213.202.211.70:26656,0e6e70a3341b45cf025d0d0576a51d774b6cba61@31.220.88.173:39656,cb825bccee49827c07dce19878c8790c67222a54@91.107.132.237:26656,d53fdcb6d01927b83e2269a4fad182e3d32643b1@65.108.8.53:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,436cb422506a1b3fc9c4e1e5920625e49babe161@185.219.142.214:26656,015a39332269be67fb95317038e8c9c57c6ca121@167.71.209.28:39656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,20da1f2c82539b0e75e818d74cb3a3dd3f8e6b63@38.242.229.208:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
