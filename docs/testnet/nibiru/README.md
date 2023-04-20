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
peers="3e7ff1b1fa8626812b1ab8acf84a8b60518a8c10@65.109.88.254:34656,daeabf9286ea1331f07f7981c5425aeca5db1f5b@95.217.5.233:26656,ac74cb4cc17470f39a575699d4979317315cacac@185.196.20.6:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,bf5be00eb2fed367f75b63b9c685ab612765e302@149.102.139.163:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,05b0e8da493f0be9fd94350da52fb59c54cc897f@161.97.150.23:26656,1da145d81ca9d5d9ccd55f529435056a27fcdeef@184.174.34.227:26656,d55b0afead31b23179fb6c2e6e514eb4b3199672@5.104.108.100:39656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,d22160eb98574ecbe437d1009e0f2284110f0626@84.46.254.232:26656,ad41ef68f4740d5be84ff54c34b0331b02ff4ae4@85.10.193.246:29656,93b0696cd10a3d683c1cf28641ff210d316954da@89.117.63.232:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,907c1095ae2abea4e5a6ba568f1fc6aa719a0d47@38.242.146.53:39656,96f253c371a7f7f854faf7ffc5e0ee9fc4f8dd7f@165.227.32.93:26656,28dbc46f1d5d2611b28c962d6094d03772baa7c9@217.76.50.20:26656,b282a25e8ad8cb6a002b9f432d29d1e57a63aeea@65.109.89.23:39656,b28dee38c03a155f4106e130ba26578a9e4552bd@130.211.192.228:26656,f4fa2e13e64628d96f9158a6a2afbb19ebac574e@85.190.246.120:26656,baa2b4dcd80073baa06ef0de6e83a0fd11cadbae@94.26.228.89:26656,2ce838eea29c3f6ca650081dd0fa99186304b151@37.99.82.28:26656,d99bb0f2616a275814bb0235c29955d6505ea677@159.27.191.170:26656,b380fa4928c0a8078b5046f6f70991395aa3f79e@91.107.232.208:26656,932f77155b5a1989096451eee2b2eb4c1a4bc48a@194.163.191.69:26656,51ed3cdd1490d47ce8846592d1ff881453dd9f93@84.46.250.179:26656,4c31b33f4266a0f769cce18f4edae08c8e267e22@38.242.237.5:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
