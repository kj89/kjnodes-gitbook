# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/jackal.png" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: lupulella-2 | **Latest Version Tag**: v2.0.0-rc.0 | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/jackal-testnet](https://explorer.kjnodes.com/jackal-testnet)

## Public endpoints

* api: [https://jackal-testnet.api.kjnodes.com](https://jackal-testnet.api.kjnodes.com)
* rpc: [https://jackal-testnet.rpc.kjnodes.com](https://jackal-testnet.rpc.kjnodes.com)
* grpc: jackal-testnet.grpc.kjnodes.com:13790

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@jackal-testnet.rpc.kjnodes.com:13756
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@jackal-testnet.rpc.kjnodes.com:13759
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/jackal-testnet/addrbook.json > $HOME/.canine/config/addrbook.json
```

**live-peers** (10)
```bash
peers="3c6d856a429224201d78c7f28026874d10a27f57@5.75.227.78:26656,344d9c933f936f79f3d62eff5cd0b82775a79dac@162.19.239.230:26656,dc84774683298e57a848b59b7c0d1a70477b4fc1@213.239.207.175:48656,27238e2f804bf28a14c186a2e0f0ceaae0d2588f@176.9.98.24:30566,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13756,f3e70d3de1974208af04dac6fabd657ab4abf0ff@65.108.75.107:24656,11b91d243d43e761c96cfbf49f2f2bd06cce2df8@65.109.23.114:17556,b549c1092e37db22576e31f19cbec4b1b3b36503@116.202.227.117:37656,80420ad774e622bda8e1dfa9b80da11eee7eed1f@144.126.140.252:29656,5eedbfbe64b942f4ab54db3842acf3bfab034c24@161.97.74.88:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
