# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/dymension.png" width="150" alt=""><figcaption></figcaption></figure>

Dymension is a network of modular blockchains called RollApps  and at the center of it all is the Dymension Hub. Dymension  allows anyone to build and deploy their own consensus-free blockchain, a RollApp.

**Chain ID**: 35-C | **Latest Version Tag**: v0.2.0-beta | **Wasm**: OFF

[Website](https://dymension.xyz/) | [Discord](https://discord.gg/dymension) | [Twitter](https://twitter.com/dymensionXYZ)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/dymension-testnet](https://explorer.kjnodes.com/dymension-testnet)

## Public endpoints

* api: [https://dymension-testnet.api.kjnodes.com](https://dymension-testnet.api.kjnodes.com)
* rpc: [https://dymension-testnet.rpc.kjnodes.com](https://dymension-testnet.rpc.kjnodes.com)
* grpc: dymension-testnet.grpc.kjnodes.com:46090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@dymension-testnet.rpc.kjnodes.com:46656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@dymension-testnet.rpc.kjnodes.com:46659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/dymension-testnet/addrbook.json > $HOME/.dymension/config/addrbook.json
```

**live-peers** (20)
```bash
peers="b8d08951d68da03af8f9272bf77684811197c289@95.216.41.160:26656,22acf9a303e825ce04171ef26e2326c09aeb238b@47.147.226.228:55656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,147a0021cff3c34251adb3ad7194574011fa3192@176.57.189.36:11656,7c720f2d079174ed7ce478b026ac3906a630d716@167.99.178.186:26656,48ea1c8c62e9eb193a317096339b22f4a4452c8c@185.144.99.22:26656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,b1e1e5a9dbf2e03b456668c2f2d9164ae090ba0c@109.123.244.56:46656,eb524a9ed0e080ec4fa9a21df3f5f56e94e0e811@51.89.7.235:26652,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,1fa5bb085e8f52c21bc71c39afbba2851bee3e18@43.157.48.181:26656,63996f52b1dc68259ff64bb2546625c71fc9d546@176.9.48.38:26656,77c42c2b2702437981976f7a648c26cd37911f7b@65.108.9.230:46656,68f6c52147c9423300f5b503348bbb02b229820c@51.159.153.211:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
