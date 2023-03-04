# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/dymension.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (20)
```bash
peers="9e1ea4938f0112c1477827344e2f9d0792710575@185.252.232.189:30656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,7b4621b7744a2c3ea5ec9453980e1d555109a746@139.162.138.158:26656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,acb69c31cac6140a1a9570e683de5e26dd008cff@51.222.44.116:32656,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,7c720f2d079174ed7ce478b026ac3906a630d716@167.99.178.186:26656,e8a706e3a81a36a6dded6cc02eabaf5d355f4c1d@80.79.5.171:28656,e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,8e667c0759bfb20ec42b939956706301a4f2a10d@65.109.92.8:26656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,db0264c412618949ce3a63cb07328d027e433372@146.19.24.101:26646,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
