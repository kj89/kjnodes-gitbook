# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (35)
```bash
peers="c171e9617904d5ab2ee7f7b5b58caab78154b703@89.117.18.185:26656,63256b5937ac438e3b21b570a07ace6ddc3bd0c6@194.163.182.122:39656,8265b2067122eff44ca4fa11a46c3381c9034bc1@65.109.163.87:26656,e634fbf8800f76cb911d03e665f2e573188147c0@154.53.32.30:26657,a5091d1afa277bab864a495d43226ee44f85604e@212.23.222.91:39656,2393cd0e22a8c70f34526fcddc99e08478c3cb7a@89.117.53.2:26656,b4583d9dd4dd03cda5f83b95edfd209f902de063@138.201.53.44:26757,10a2db5117fe9fdfefcfc9ca633e5633b0c38d4e@34.125.211.20:26656,4fb43c4d6bd6cf0f20781b67e437263a24e4153d@95.217.75.105:31656,224c85918ea98d62daab63ba9eceab195b676760@144.91.71.1:26656,d622efcde775f33bd8c14fa5757ee9fa95d4149e@135.181.203.53:26656,cc5eac998dbd8d1c21ac293f1c946f1bb1583826@185.237.253.248:26656,aaff99ce425ac9d062d1bca6f75987656e137307@138.201.34.19:26656,f41685745f7cd74caa542829d291367ae1377ce0@34.74.30.133:26656,022c0e642eefa50a78e9e03bb1fa80237da232ac@178.208.252.54:28656,9a46a84b86410636540e7405e8d76ed4740b6bb7@46.151.26.153:26656,452e0e07750f380d87e1bd654a198df0c1225130@80.82.215.59:39656,7b3ebcf55ea111436056214743aad227672b3e6d@5.181.190.161:26757,b6db16ab4d2dfd61d0be94df4738ce5f1913de11@212.41.9.98:26656,879d464755722009c853f748f04f729e4cd8b368@116.202.227.117:39656,57cd99659f4895cada5ba5a9f594ce9a5fdb0fa8@46.4.23.42:46656,4e3f67a4c88b40045e0de521bab5a3cee9aeb4aa@139.217.229.125:26656,bce7435b6231fd97885ffccc57b1d7d98f20b37f@173.212.235.229:26656,ed02182dfbfdd209003fae545f1065330f69ef27@138.201.22.238:26646,d3bacf8624684354d0676320bc5556e1e893bdfa@65.21.91.50:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,07d59fc815394526696a364ef4c6910683c332e7@139.144.97.186:26656,e387712543bc99c6719f7975ee75e48afb99b088@66.45.251.38:60656,6c679a2b8397b1d04a33de37828e3b67e9e6b9c0@65.109.6.21:27656,1edd1232fe59fd00a13bfdd9ac273e48b20f11c3@65.108.231.124:12656,e9597b5074802ca53eb630a07603093e7ee98e6f@212.90.121.51:26656,35d8f676cf4db0f4ed7f3a8750daf8010797bdc4@135.181.116.109:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,3a5ba67e5329791db55763354ff98d3c253e4a0c@103.136.249.27:26656,9d5557755cf50a274ab5bada66cf26db64da296b@135.181.119.59:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
