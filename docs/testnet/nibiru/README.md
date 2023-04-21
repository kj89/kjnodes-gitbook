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
peers="452a3e2dda1f044221f30a8e25e6b90eaef70ce1@154.26.157.17:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,467010d590de6aab28f95ee4403d2da3463dc203@144.91.103.115:26656,fd0379ae2ef2bfb7f174d0171c06f0bc5bcd286f@183.2.149.136:26656,2ce838eea29c3f6ca650081dd0fa99186304b151@37.99.82.28:26656,ad41ef68f4740d5be84ff54c34b0331b02ff4ae4@85.10.193.246:29656,f31536c1f70fb1a8127c1f412bbccef4d1a19e20@195.14.6.2:26656,6ed1a9222eb38742eec37cf9a3556aa8fa5b4b18@84.46.249.197:26656,c73ede442d5e3efe36cec58c834257c417b973a7@38.242.129.14:39656,ca05a8a7ce9f92b8851ec941030e0670cd4ccc00@1.52.218.176:26656,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656,f4fa2e13e64628d96f9158a6a2afbb19ebac574e@85.190.246.120:26656,a6062857b20b62693523643cb19dc0f3dd4ee961@90.188.249.252:26656,93b0696cd10a3d683c1cf28641ff210d316954da@89.117.63.232:26656,a5455fdd70a915023bb4902143704430793c3e68@162.55.163.78:26656,38f93e80523c985e8231a67299b52ee75faad192@81.0.218.88:26656,88f4766708602357ab66982bc6c48f8e34b22cfc@2.58.82.127:39656,1e886c522cd043092062bec284e3f87a3e310b2f@45.8.133.159:26656,4a44af55ee65d15c13d666bb5d830da43673f7a9@185.190.140.80:26656,10d32d2262e7a1d79c4283cef696a521dec43785@85.239.233.155:10656,46c0cb4d56ebfd4c69911c59b3f17cb17bcc3ed7@64.226.94.147:26656,4177714e7af5ab9c3500cac6dca4e4a6a4912c48@194.242.57.215:26656,5628aabefa8edc3def27bdf4cb966089939f36a7@213.202.218.60:26656,39ce82b6613c327f2bbc4cedc3a25dbf0bf8094e@38.242.252.137:26656,daeabf9286ea1331f07f7981c5425aeca5db1f5b@95.217.5.233:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,ac74cb4cc17470f39a575699d4979317315cacac@185.196.20.6:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
