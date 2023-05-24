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

**live-peers** (10)
```bash
peers="b473a649e58b49bc62b557e94d35a2c8c0ee9375@95.214.53.46:36656,869d03182da215ae0171ac37ee69a77ed59d1a38@135.181.253.11:46656,e5226fa166386f9055908194a4942c06b7003ab5@65.108.192.123:42656,82b51653205df40d43f257041db2da0f9f1644fa@178.63.26.94:46656,7bbce7809296bf484ffcef6235550e03770cf81b@5.9.147.20:26656,513557be25d2edc51481be90c808f72cd662e1d2@167.235.250.107:26656,f4be55edab4b5cb40464aa50def5d2cd39359e67@185.182.185.101:26656,bb8615bb51139c05fd59020fc2aa7eac210690b4@135.181.221.186:27656,d2b841acdcabb622e9033fe685a395eef091f2fe@65.108.199.62:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
