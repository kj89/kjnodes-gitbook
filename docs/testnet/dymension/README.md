# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/dymension.png" width="150" alt=""><figcaption></figcaption></figure>

Dymension is a network of modular blockchains called RollApps  and at the center of it all is the Dymension Hub. Dymension  allows anyone to build and deploy their own consensus-free blockchain, a RollApp.

**Chain ID**: 35-C | **Latest Version Tag**: v0.2.0-beta | **Wasm**: OFF

[Website](https://dymension.xyz/) | [Discord](https://discord.gg/dymension) | [Twitter](https://twitter.com/dymensionXYZ)




## Chain explorer
[https://explorer.kjnodes.com/dymension-testnet](https://explorer.kjnodes.com/dymension-testnet)

## Public endpoints

* api: [https://dymension-testnet.api.kjnodes.com](https://dymension-testnet.api.kjnodes.com)
* rpc: [https://dymension-testnet.rpc.kjnodes.com](https://dymension-testnet.rpc.kjnodes.com)
* grpc: [https://dymension-testnet.grpc.kjnodes.com](https://dymension-testnet.grpc.kjnodes.com)

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
peers="e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,8e667c0759bfb20ec42b939956706301a4f2a10d@65.109.92.8:26656,88fdaf5ff074dc2010ccb0416e421f3819201eb6@212.23.222.125:30586,3c937029e41e3f7b92b8b87d787be0ddc2a3f13c@70.34.214.236:26656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,6ee2e6550cd3510c0fc912bf0632a894148a79a7@38.242.202.174:31656,af97c76448e6a5d7671c6523f38fc48cc7273da7@217.76.59.46:26656,e6ea3444ac85302c336000ac036f4d86b97b3d3e@38.146.3.199:20556,6229800969107d039254a8e6888aaeb464cda44d@167.99.186.186:26656,0d30a0790a216d01c9759ab48192d9154381e6c0@136.243.88.91:3240,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,80cce834fc749c0a9f47182665f833f97170ff4b@65.108.104.167:46656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,015c628c6975befaaec912a88f19c0566f37173e@95.217.133.45:46656,65242d54d20a6c16a401004a8fb936343d9cae99@65.109.106.91:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
