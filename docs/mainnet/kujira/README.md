# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

[Website](https://kujira.app) | [Discord](https://discord.gg/teamkujira) | [Twitter](https://twitter.com/TeamKujira)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym)

## Restake

[Restake with kjnodes](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/kujira](https://explorer.kjnodes.com/kujira)

## Public endpoints

* api: [https://kujira.api.kjnodes.com](https://kujira.api.kjnodes.com)
* rpc: [https://kujira.rpc.kjnodes.com](https://kujira.rpc.kjnodes.com)
* grpc: [https://kujira.grpc.kjnodes.com](https://kujira.grpc.kjnodes.com)

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

**live-peers** (18)
```bash
peers="5ae54af5483ff090e57a51f9f3568490373e2419@135.181.26.211:26656,b8e8c1738a49cd6143cf83287a5087c2618ebca0@141.95.47.82:30256,27227b6c380d806bc9c934bdbd8ca060fb61d7df@217.174.247.59:15602,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,8df276d9873c0ab16a911c5f779caa6f121c845e@89.163.145.138:26656,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,89757803f40da51678451735445ad40d5b15e059@169.155.45.187:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@95.217.70.62:26656,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,c1a740841a6dc0b56730e975b1a4aa2d8c73b204@65.108.237.233:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
