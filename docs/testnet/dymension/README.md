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
peers="1135bf4bf8ffad1b9b508ea6c7408085ec87563a@134.122.16.44:26656,c36184fec2fb60bf7be775390c1cd6619c0201ef@209.126.81.240:26656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,22acf9a303e825ce04171ef26e2326c09aeb238b@47.147.226.228:55656,e374d21e689d4e1832ef72e0dae2a9bca435ba36@95.217.114.220:46656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,c7a36d7abeea5704290f99c1608b50ff1f5e3e47@79.143.188.183:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,6ebe5856a7617cb9309a923a3935687903d2607d@141.95.97.28:15256,39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,63996f52b1dc68259ff64bb2546625c71fc9d546@176.9.48.38:26656,ca2cfea3c48640c094ad740bb41c2aeb81b5dcc6@194.163.187.175:46656,b1e1e5a9dbf2e03b456668c2f2d9164ae090ba0c@109.123.244.56:46656,54160abe97cd71abb3a83516fd8e4a47cb509fba@188.34.178.103:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
