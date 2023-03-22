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

**live-peers** (19)
```bash
peers="39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,63996f52b1dc68259ff64bb2546625c71fc9d546@176.9.48.38:26656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,b8d08951d68da03af8f9272bf77684811197c289@95.216.41.160:26656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,ca2cfea3c48640c094ad740bb41c2aeb81b5dcc6@194.163.187.175:46656,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,22acf9a303e825ce04171ef26e2326c09aeb238b@47.147.226.228:55656,48ea1c8c62e9eb193a317096339b22f4a4452c8c@185.144.99.22:26656,7c720f2d079174ed7ce478b026ac3906a630d716@167.99.178.186:26656,a8475788f47e385cba9f505c7c6de95124377212@142.132.178.2:26656,44df333024cebe9b8e8361ac67feaa930ec6dc1f@65.109.85.170:54656,4c25618c9465c0aaea91d936be446d5db04be3d1@195.201.237.185:46656,147a0021cff3c34251adb3ad7194574011fa3192@176.57.189.36:11656,e678f78d3250fef1e6e0afcdb1ebdc5fe0d7138c@5.161.76.147:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
