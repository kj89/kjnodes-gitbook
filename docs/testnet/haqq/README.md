# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/haqq.png" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.1 | **Wasm**: OFF

[Website](https://islamiccoin.net) | [Discord](https://discord.gg/hU9MHG5kZq) | [Twitter](https://twitter.com/Islamic_Coin)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/haqq-testnet](https://explorer.kjnodes.com/haqq-testnet)

## Public endpoints

* api: [https://haqq-testnet.api.kjnodes.com](https://haqq-testnet.api.kjnodes.com)
* rpc: [https://haqq-testnet.rpc.kjnodes.com](https://haqq-testnet.rpc.kjnodes.com)
* grpc: haqq-testnet.grpc.kjnodes.com:13590

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@haqq-testnet.rpc.kjnodes.com:13556
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@haqq-testnet.rpc.kjnodes.com:13559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/haqq-testnet/addrbook.json > $HOME/.haqqd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,b87ae2a43e27bd0360ea1b868c8cb9e98d612fce@65.109.92.79:19656,f54d4de6d4ae81ec8a2315b54247872b315f198d@65.109.57.9:26656,a6150d39e4725d28a56f41ebf3c6d457c54bd2f1@34.138.250.4:26656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,306ce653d6f0c77936b681d4ee8bbf66a4b8bb75@88.208.57.200:60956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13556,5c11c697aaf2dabf96e3eb7e7e621c200bd309ee@65.21.225.58:26656,26f20a2f80a4738a30a9634947a3aae67da31be3@65.108.254.227:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
