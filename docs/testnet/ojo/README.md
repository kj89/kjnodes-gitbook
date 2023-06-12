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
peers="978cf9aca38f819fd8189272379fc3c2ae2682a8@213.239.218.210:56656,e27836973284ea7c16dbdc23556bac489042cd8d@37.187.142.41:26656,8036aed2d37890ddf245e7288b4fc724a301d728@65.109.117.23:50656,18300f0a5973798c3900fe51ff255bb6bca982f9@65.109.65.248:36656,ffe2d5ecb614762d5a1723f5f8b00d3feb6eb091@5.9.13.234:26686,69774d64905bb33ea805228ac875835aea09f25a@185.217.198.141:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,d6b0791afd2d41c47bce8c152174b40c230988ba@138.201.225.104:47756,5a53ebe6e029f8a26b1bc6dd8fe9a8efd57202f6@167.71.194.75:28656,f6d6e625759814e157457a5889961e02dba26ba6@65.109.92.240:37096"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
