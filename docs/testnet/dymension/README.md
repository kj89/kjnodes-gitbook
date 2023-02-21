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

**live-peers** (10)
```bash
peers="39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,b1e1e5a9dbf2e03b456668c2f2d9164ae090ba0c@109.123.244.56:46656,57f2f7cd86e69806dc3f1b752af97add04e96558@5.161.55.248:26656,547cf669555bd611ba57b37bb0f288793ea4ec49@141.94.138.48:26673,65242d54d20a6c16a401004a8fb936343d9cae99@65.109.106.91:26656,6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,e374d21e689d4e1832ef72e0dae2a9bca435ba36@95.217.114.220:46656,eb524a9ed0e080ec4fa9a21df3f5f56e94e0e811@51.89.7.235:26652,488a1665d94f257733b04f7b4fbcef058cbb11cd@65.108.199.206:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
