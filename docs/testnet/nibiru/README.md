# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibirufi) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:13990

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:13956
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:13959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (19)
```bash
peers="afe25edd4b7515d5f013112166e157e4289177bb@95.217.35.186:46656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,d88eb958f18940d75add40b51d2a69295ed9e378@5.75.245.162:26656,04c7b4c7b1ca40e04e767925c08846d2951f5425@34.23.168.27:26656,6173aa0fb340ab41724d72339d164a86e7a6d0ac@185.229.119.95:26656,c20a499a21668237d67b44d44623aaebedbea81f@173.249.20.170:26656,4af344bb3302bf926580f0b8ea4de9be401c3522@94.131.111.156:26656,1b68638343f79c9634ed67923aa8e3ec46c18516@91.142.77.13:26656,954598490831bce4e650593d23466bf676c04914@185.16.39.19:38656,d68895141d74eadfb1b620955102ad2db6b1d9ea@51.195.88.136:15662,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,b87fb99a9a4b6d2651b4015ff7f055a82ea6acdd@116.202.17.68:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,e774ca76b7765c49e21daff712fbbc93815771ab@5.9.70.180:15662"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
