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
peers="1fa5bb085e8f52c21bc71c39afbba2851bee3e18@43.157.48.181:26656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,c38a57e1ed990ae7f15479f302b7b565335815c3@65.109.156.208:05656,bb8615bb51139c05fd59020fc2aa7eac210690b4@135.181.221.186:27656,513557be25d2edc51481be90c808f72cd662e1d2@167.235.250.107:26656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,b8d08951d68da03af8f9272bf77684811197c289@95.216.41.160:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
