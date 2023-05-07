# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/dymension.png" alt=""><figcaption></figcaption></figure>

Dymension is a network of modular blockchains called RollApps  and at the center of it all is the Dymension Hub. Dymension  allows anyone to build and deploy their own consensus-free blockchain, a RollApp.

**Chain ID**: 35-C | **Latest Version Tag**: v0.2.0-beta | **Wasm**: OFF

[Website](https://dymension.xyz/) | [Discord](https://discord.gg/dymension) | [Twitter](https://twitter.com/dymensionXYZ)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/dymension-testnet](https://explorer.kjnodes.com/dymension-testnet)

## Public endpoints

* api: [https://dymension-testnet.api.kjnodes.com](https://dymension-testnet.api.kjnodes.com)
* rpc: [https://dymension-testnet.rpc.kjnodes.com](https://dymension-testnet.rpc.kjnodes.com)
* grpc: dymension-testnet.grpc.kjnodes.com:14690

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@dymension-testnet.rpc.kjnodes.com:14656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@dymension-testnet.rpc.kjnodes.com:14659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/dymension-testnet/addrbook.json > $HOME/.dymension/config/addrbook.json
```

**live-peers** (11)
```bash
peers="bb8615bb51139c05fd59020fc2aa7eac210690b4@135.181.221.186:27656,95f016933b6b25a44a3b1257a45af1db3335ae61@65.109.30.110:11773,68f6c52147c9423300f5b503348bbb02b229820c@51.159.153.211:26656,8c3d6e4d065c6c171e2620f8ed8be5404fa61923@162.55.1.176:26656,8e667c0759bfb20ec42b939956706301a4f2a10d@65.109.92.8:26656,b473a649e58b49bc62b557e94d35a2c8c0ee9375@95.214.53.46:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,5dbbb68e0c8a86bdc372cf1de0691f1cdc6a96ad@82.208.23.223:27656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
