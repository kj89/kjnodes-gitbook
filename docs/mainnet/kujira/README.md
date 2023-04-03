# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.8.4-mainnet | **Wasm**: ON

[Website](https://kujira.app) | [Discord](https://discord.gg/teamkujira) | [Twitter](https://twitter.com/TeamKujira)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/kujira](https://explorer.kjnodes.com/kujira)

## Public endpoints

* api: [https://kujira.api.kjnodes.com](https://kujira.api.kjnodes.com)
* rpc: [https://kujira.rpc.kjnodes.com](https://kujira.rpc.kjnodes.com)
* grpc: kujira.grpc.kjnodes.com:13090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@kujira.rpc.kjnodes.com:13656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@kujira.rpc.kjnodes.com:13659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/kujira/addrbook.json > $HOME/.kujira/config/addrbook.json
```

**live-peers** (15)
```bash
peers="9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,7878121e8fa201c836c8c0a95b6a9c7ac6e5b101@51.161.117.214:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,3457c7c0ff7c368c35f0d574a289d5ef77b504b7@65.108.9.164:10656,d6d14f99ef25c8ffee6fa4afca40fece0c1ab9fe@107.181.229.154:20656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,fdde823fb8c9ef908d4b229f177c5f8b18e90274@54.235.174.123:26656,c55d35ef908b74c2ddec2f47dbdb4032d7dfbcd4@23.88.69.22:27266,de08e6178779ff3b19a8b6d22a05664392cb2b35@185.216.179.205:26656,6f3129d01218b939511cccf7e0318bfe872d97c4@65.109.33.181:26656,bd2821b2dc8b928946026caf3e9bd1e7a0013a61@145.239.10.46:13656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
