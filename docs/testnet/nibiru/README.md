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

**live-peers** (29)
```bash
peers="10b77a4ab480c05e323a401b493a08dca2a3ec48@154.53.42.141:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,0e6e70a3341b45cf025d0d0576a51d774b6cba61@31.220.88.173:39656,ad41ef68f4740d5be84ff54c34b0331b02ff4ae4@85.10.193.246:29656,2ce838eea29c3f6ca650081dd0fa99186304b151@37.99.82.28:26656,452a3e2dda1f044221f30a8e25e6b90eaef70ce1@154.26.157.17:26656,6ed1a9222eb38742eec37cf9a3556aa8fa5b4b18@84.46.249.197:26656,467010d590de6aab28f95ee4403d2da3463dc203@144.91.103.115:26656,daeabf9286ea1331f07f7981c5425aeca5db1f5b@95.217.5.233:26656,359ab5a45015c75b0ca847519254cb8d0aa3aa6c@65.108.206.74:26656,93b0696cd10a3d683c1cf28641ff210d316954da@89.117.63.232:26656,c4c1285236515db8170f959433a9dc1277ba2abe@185.135.137.236:26656,f4a8fb180fbbb4c44e7721368cbc6ce3f9fc47e1@5.189.140.55:26656,96f253c371a7f7f854faf7ffc5e0ee9fc4f8dd7f@165.227.32.93:26656,00b1c55019204641cada3f3f24d0c191f760745f@194.163.149.195:26656,e1a8a5f0b0d6ad3a2e39560dc282f96ff023919d@77.220.215.44:26656,bf5be00eb2fed367f75b63b9c685ab612765e302@149.102.139.163:26656,64cf20514a03108936e27b9382c228d42b4642e1@88.198.14.157:26656,4177714e7af5ab9c3500cac6dca4e4a6a4912c48@194.242.57.215:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,d0c580a19e635fdb2d60d56b9462c0aa4e4517d6@207.180.227.122:26656,f4fa2e13e64628d96f9158a6a2afbb19ebac574e@85.190.246.120:26656,87db46e4d447f47ebe7efc15109f60abeaa2333d@38.242.130.95:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,0e90ac8e15b040c2a158b68f25299fc32a9d5940@89.117.57.25:26656,b2dfeee10a366deae4ed6f142d2c99a9dc35577a@109.123.243.187:26656,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656,785ffb99f8724319d44254cbb47b3428aaaa25a5@38.242.236.134:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
