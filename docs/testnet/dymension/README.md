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
peers="4c25618c9465c0aaea91d936be446d5db04be3d1@195.201.237.185:46656,b1e1e5a9dbf2e03b456668c2f2d9164ae090ba0c@109.123.244.56:46656,64acca240c1149f94b8986ffea3ee1b4e0bd5fbe@45.150.64.115:26656,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,ed76fabd897c8911942ac4fa1c91f3f0afa7fdda@65.108.225.70:26656,56e0f891f8312e239a631aea2f8b0e64c9f7d824@135.181.95.145:36656,80cce834fc749c0a9f47182665f833f97170ff4b@65.108.104.167:46656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,8e667c0759bfb20ec42b939956706301a4f2a10d@65.109.92.8:26656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,63996f52b1dc68259ff64bb2546625c71fc9d546@176.9.48.38:26656,39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,ca2cfea3c48640c094ad740bb41c2aeb81b5dcc6@194.163.187.175:46656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,1135bf4bf8ffad1b9b508ea6c7408085ec87563a@134.122.16.44:26656,b8d08951d68da03af8f9272bf77684811197c289@95.216.41.160:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
