# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nois.png" alt=""><figcaption></figcaption></figure>

Nois Network aims to bring randomness (or noise)  to the Cosmos ecosystem by providing a safe and  secure entropy source and distributing randomness  in the form of random beacons to other Cosmos blockchains via IBC.

**Chain ID**: nois-1 | **Latest Version Tag**: v1.0.3 | **Wasm**: ON

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
peers="b26e5ac4afbadf96ad31ee3aeb5e6557f2894037@65.108.199.222:30656,288e7a14ccac3cdc1d8ab20335d4c48edf5930f2@84.46.250.136:17356,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27286,7bd2beda636ef3077d349a0bacf6fca87c8d9b65@144.76.63.67:26806,732fe2553e152d37b29653ee07324fdbfd5ef961@95.217.200.26:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15156,6ef1914f30ac7becdf2c718b65c61cd618b7021a@57.128.144.242:26656,c695f41458b08fe87729beffa513f1c38d20d1db@193.70.33.64:17356,40692288807db7ac022e24e9247cd60e7fc995c7@81.0.248.57:17356,d2041f5d812b4fb196d5210a287448b68fe7bef9@95.217.104.49:51656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
