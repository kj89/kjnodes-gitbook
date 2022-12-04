# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.1.0 | **Wasm**: OFF

Website: [https://www.defund.app](https://www.defund.app)


## Public endpoints

* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (27)
```
peers="d325bc4677b9a10d9acc2f34982f8001099e7e2b@88.210.6.152:26656,672adb4f349b23e7d408d9b01477eabe7523249b@178.18.245.208:40656,62df45d2df885de6dd2230dccf975a04005d23b3@164.68.121.197:40656,8a865d76928017ad8e889b91b4d52bfb88526392@45.67.229.12:26656,ce919107c495d85a20d37bb599bff42d843e4bac@45.144.29.185:26656,312e78a4ba124a1cc92f71d37a603c425ceb4d1b@199.175.98.108:26656,89944fe8fc90920cdd95ac8b752b81524c357961@38.242.234.75:26656,92b8be11b64cd5b81a445b6d04d50292fc2d3b33@194.146.13.180:26656,e4470dac98f2cee5bd060c52c7d801d57bfc9308@185.245.182.206:26656,e8fd4ce8e97ff75fd76934c0da242bb872d28ad0@199.175.98.109:26656,4c291b33574d679e43f7cec340ba4befecec0724@161.97.152.115:26656,195f80fa7d564efd62304bcb7da85f0a50f3d7db@109.123.254.113:26656,5e6354412f3742ac76e37838236707b373c1de43@185.250.37.162:29656,6ad4f3be13155729927f0af19ceb08f89477798d@75.119.131.75:26656,5ac40e96d9194536e15a28a1010551300cbab616@185.216.75.21:26656,b1e1758323425265c1db42b0fbaa7ab80612a582@38.242.207.15:40656,ef4cac7e5813a753239239e297efcabc03a07fbb@194.180.176.125:26656,aa0f97cda5bd962821b907245dc476348309fce3@84.21.171.33:40656,f98092af7d5aa5fedb2af24200eb4ceeb252a007@91.194.11.115:26656,68b4a53b3b67da6a4736888c36074eb316ea510d@75.119.157.222:26656,f17140ac29380d434c1b5d2e33798d9f3bc6fd45@209.126.2.211:26656,d3334ae0a1608e3418ba09a1f7a079163960a46f@38.242.235.216:26656,d70dc31f93642a557a8d4668654c333784338331@154.53.57.72:26656,9219fe3a1e0759bd4aa18ca3022c62f019e42c86@185.187.169.237:26656,879e60e820e318038b7ee2238560d5d32999deed@38.242.206.61:40656,695eb6029f2749c4661b716b9b9e110e0bdc5356@62.171.147.78:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
