# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nois.png" alt=""><figcaption></figcaption></figure>

Nois Network aims to bring randomness (or noise)  to the Cosmos ecosystem by providing a safe and  secure entropy source and distributing randomness  in the form of random beacons to other Cosmos blockchains via IBC.

**Chain ID**: nois-1 | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://nois.network) | [Discord](https://discord.gg/dHdpwtEb6F) | [Twitter](https://twitter.com/NoisRNG)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/nois/noisvaloper1fe7ju873fkknmfrmytaft93y5rlf0xcrqtp39k)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/nois/noisvaloper1fe7ju873fkknmfrmytaft93y5rlf0xcrqtp39k) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/nois](https://explorer.kjnodes.com/nois)

## Public endpoints

* api: [https://nois.api.kjnodes.com](https://nois.api.kjnodes.com)
* rpc: [https://nois.rpc.kjnodes.com](https://nois.rpc.kjnodes.com)
* grpc: nois.grpc.kjnodes.com:15190

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@nois.rpc.kjnodes.com:15156
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@nois.rpc.kjnodes.com:15159
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nois/addrbook.json > $HOME/.noisd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="c86b0c3ffb4fa65b188ac68d2872a9d91559bce1@65.21.55.133:26656,379c0e32463be66e5cf8d13d62eb87ddb1a702c2@142.132.152.46:47656,763f4cd38f0685616b6657d9a34c1cdbf01ca90c@212.23.222.109:26456,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15156,9d21af60ad2568ffcb55a0bd0eb03b6cfa2644c5@49.12.120.113:26656,ae02b0a36568a1f2be71bd98840aae333d1e3147@51.159.195.168:46656,eeb51b9e6c7d6de977e3c6419f3bba78263b4b7e@192.99.32.49:26656,9620f8453f34270be5fa3d458968d8bd1c997430@95.70.184.178:29656,b26e5ac4afbadf96ad31ee3aeb5e6557f2894037@65.108.199.222:30656,d4f30672ef58f234fd13b503f7ca3d32ffc4e7a2@45.63.104.164:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
