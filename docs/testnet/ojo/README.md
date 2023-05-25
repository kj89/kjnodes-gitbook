# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ojo.png" alt=""><figcaption></figcaption></figure>

Ojo is a decentralized security-first oracle network built  to support the Cosmos Ecosystem. Ojo will source price data  from a diverse catalog of on and off-chain sources and use  advanced security mechanisms to guarantee the integrity of the data it provides.

**Chain ID**: ojo-devnet | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://ojo.network) | [Discord](https://discord.gg/fd8Yrex8nC) | [Twitter](https://twitter.com/ojo_network)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/ojo-testnet](https://explorer.kjnodes.com/ojo-testnet)

## Public endpoints

* api: [https://ojo-testnet.api.kjnodes.com](https://ojo-testnet.api.kjnodes.com)
* rpc: [https://ojo-testnet.rpc.kjnodes.com](https://ojo-testnet.rpc.kjnodes.com)
* grpc: ojo-testnet.grpc.kjnodes.com:15090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ojo-testnet.rpc.kjnodes.com:15056
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ojo-testnet.rpc.kjnodes.com:15059
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ojo-testnet/addrbook.json > $HOME/.ojo/config/addrbook.json
```

**live-peers** (10)
```bash
peers="bfdeba21ca39394ab264fff9c16188b6ecdace6d@144.91.82.61:26656,b16d876c443850cd358596790411b835d3f1735b@95.214.53.46:35656,98a552530acb9b0e81a834c2f514ee962da2bddf@65.109.70.45:16656,59954989ec7cb0c12ec55128d142db1a274b4465@135.181.221.186:26656,46be755bb7f34a6f4722713e40c9786266654396@38.242.237.125:26656,ec003ade1f7c57d822a1be56c838e668b755bee5@94.190.90.38:33656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,e3d56e1538e41115bccdcb0b83a734407d59d2b9@185.219.142.216:50656,bd90b71f1f982ebb18857da8cb777883d6ca687e@185.209.223.68:26656,4bfc6d62d115a2440f9e5dc10c21d302dbdf5c64@34.220.136.165:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
