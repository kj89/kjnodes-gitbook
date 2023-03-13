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

**live-peers** (18)
```bash
peers="e6ea3444ac85302c336000ac036f4d86b97b3d3e@38.146.3.199:20556,6229800969107d039254a8e6888aaeb464cda44d@167.99.186.186:26656,be789ab36bc298b491735f2313d5f99abf452d1f@162.55.246.165:26656,8e667c0759bfb20ec42b939956706301a4f2a10d@65.109.92.8:26656,015c628c6975befaaec912a88f19c0566f37173e@95.217.133.45:46656,e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,236b71988898dff63cef139f83a64f5fbfd9d8d7@135.181.18.112:55696,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,80cce834fc749c0a9f47182665f833f97170ff4b@65.108.104.167:46656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656,f8175ce7bc19d015ec17083fe19b80eae2bd2a9c@65.21.239.60:46656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,6c0ddab56755cd010f65f1f1201d29120a2d9092@38.242.202.200:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
