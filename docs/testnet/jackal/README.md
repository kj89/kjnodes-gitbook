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
peers="2ededbdbd98580e22ae8c3676e37b6e1fc1d987b@142.132.248.253:23656,a0f726a3dffb45d9cbde0913701bd757fcd7e434@157.90.2.254:36656,dc84774683298e57a848b59b7c0d1a70477b4fc1@213.239.207.175:48656,5eedbfbe64b942f4ab54db3842acf3bfab034c24@161.97.74.88:46656,bda5e61d05f423919783ff73dc096ac3a8eef5c3@65.108.57.170:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13756,e4e93ce4b050c9d821e15b69477f5da706121343@65.109.93.152:31656,34bb04a3e226493e5d142c74bf78d2ed2803ee9d@213.133.100.172:27464,80420ad774e622bda8e1dfa9b80da11eee7eed1f@144.126.140.252:29656,451622fd913f6119a67f67e65f3ab82c3fbea529@78.107.253.133:32656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
