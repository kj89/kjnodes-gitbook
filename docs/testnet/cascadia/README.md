# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" alt=""><figcaption></figcaption></figure>

Cascadia is a layer-1 blockchain built to explore the  nature of incentives on network effects, starting  with ve-tokenomics.

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://www.cascadia.foundation) | [Discord](https://discord.gg/cascadia) | [Twitter](https://twitter.com/CascadiaSystems)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cascadia-testnet](https://explorer.kjnodes.com/cascadia-testnet)

## Public endpoints

* api: [https://cascadia-testnet.api.kjnodes.com](https://cascadia-testnet.api.kjnodes.com)
* rpc: [https://cascadia-testnet.rpc.kjnodes.com](https://cascadia-testnet.rpc.kjnodes.com)
* grpc: cascadia-testnet.grpc.kjnodes.com:15590

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@cascadia-testnet.rpc.kjnodes.com:15556
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@cascadia-testnet.rpc.kjnodes.com:15559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/addrbook.json > $HOME/.cascadiad/config/addrbook.json
```

**live-peers** (11)
```bash
peers="e6e3fbc13c1903ac758ce7c6fa180312b89af2e8@142.132.248.253:25656,0887cadb47c1288050aa7626dc31585d2ba5bb5e@38.242.146.152:26656,85b0fba108b64481b025262c1fea99d32037654b@75.119.147.244:26656,4ec51eeff609e98100beb77bfb34fec9add6057d@45.14.194.130:18656,1d61222b7b8e180aacebfd57fbd2d8ab95ebdc4c@65.109.93.152:35656,0fb3f783deef83ae92deb9e913577b8623008cd1@65.108.48.40:18656,9e7532d74929bee30a2ac1f8628aca46191684ef@194.163.156.184:18656,b71287a85b70df75e1405c6831634738e6b957ab@65.108.72.253:15656,cf1a8643134d7c5378d7af1e426e1ada46881f6c@5.78.78.201:18656,40739dda0aa1fd152faecfd540ddb876481fa7b2@170.64.158.48:18656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
