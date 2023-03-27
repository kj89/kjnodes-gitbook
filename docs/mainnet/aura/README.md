# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/aura.png" width="150" alt=""><figcaption></figcaption></figure>

The Aura Network protocol allows users to mint, rate, track data,  or trade NFT for the goal of constructing a strong platform to  support all trading assets on the crypto market in a simpler and easier way

**Chain ID**: xstaxy-1 | **Latest Version Tag**: aura_v0.4.4 | **Wasm**: ON

[Website](https://aura.network) | [Discord](https://discord.gg/hpvF5QcWRf) | [Twitter](https://twitter.com/AuraNetworkHQ)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/aura](https://explorer.kjnodes.com/aura)

## Public endpoints

* api: [https://aura.api.kjnodes.com](https://aura.api.kjnodes.com)
* rpc: [https://aura.rpc.kjnodes.com](https://aura.rpc.kjnodes.com)
* grpc: aura.grpc.kjnodes.com:17090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@aura.rpc.kjnodes.com:17656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@aura.rpc.kjnodes.com:17659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/aura/addrbook.json > $HOME/.aura/config/addrbook.json
```

**live-peers** (20)
```bash
peers="a58b4dec687b60ba05cf9a3e4cd1181b09c0661f@65.109.93.152:34656,ed15ae05f17dd4e672eec0a96c38364d063b68dc@65.108.6.45:60756,edbd221ceecf4e0234fb60d617a025c6b0e56bf0@178.250.154.15:36656,3e7ef25f1c9829351936884618659167400eb0f1@142.132.149.171:26656,f67f9a6f5121b6388c84812a812d5d6eca0b39e8@148.251.66.248:26656,5d9146e9446df65ac30dd0a2dcb7e5887aaa6fa6@188.40.67.160:26656,a1f949c765bfc493ddd2e0e8477170bcc3b86a57@194.163.179.176:16656,0179528068da0dfaf61005cf5aa28793ca42b129@85.25.74.163:26656,ed68064620cebd196f56335bf801144efa9fb5ef@185.22.232.82:26656,b91ee5c72905bc49beed2720bb882c923c68fbc9@80.92.206.66:26656,dc9c2ab4055a2ef8ddca435e9d8c120969562f98@194.247.13.139:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:17656,0d9dead3ba3a6bc8a6e650c2d41e3beae924b444@81.0.220.94:25056,a19b89ebbf7331f435b8ef100ce501d2377922ea@209.126.116.182:26656,c2215f1673d21a7462f38bf7fbd16f8567393f7c@13.251.159.166:26656,abb367c73ef28fc90f5071e1258a23c0e5be17cd@103.107.183.89:26656,c9c0b28dcf2db5f0e7b756986d3326d62ba47e78@144.126.147.58:26656,a60a9f3400cb978b313ad5a47d59f6c518ef2a04@3.135.201.61:26656,dd6474ec049a264abd25248f0fd9178058331fe0@54.179.159.96:26656,e46238ddcf2113b70f59b417994c375e2d67e265@71.236.119.108:40656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.aura/config/config.toml
```
