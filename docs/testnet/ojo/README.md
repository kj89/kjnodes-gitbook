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
peers="b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,f35a6ea4693d24d3727a8e866acab2a9faa2ddbc@91.223.3.144:26256,8036aed2d37890ddf245e7288b4fc724a301d728@65.109.117.23:50656,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,7d59fd87e149226d58d28846a17711ec8b89888c@65.109.122.105:60956,8617d456081aab4798ea323193b07b9b434b5e49@146.190.132.147:15056,a3b980ccdcf7146fc4a412fb10ad170682263832@62.171.162.229:50656,bd90b71f1f982ebb18857da8cb777883d6ca687e@185.209.223.68:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
